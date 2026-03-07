from flask import Flask, request, jsonify, render_template

import os

from cryptography.fernet import Fernet

from nrclex import NRCLex



app = Flask(__name__)



# Store keys simply in a dict (for demonstration purposes)

keys_store = {}



def extract_top_emotions(text):

    text_lower = text.lower()

    emotions_found = set()

    

    # Custom keyword mapping to catch nuanced emotional combinations

    keyword_map = {

        'Joy': ['happy', 'joyful', 'ecstatic', 'thrilled', 'glad', 'delighted'],

        'Anxiety': ['anxious', 'nervous', 'worried', 'stress', 'fear', 'anxiety'],

        'Sadness': ['sad', 'failed', 'disappointed', 'depressed', 'cry', 'upset'],

        'Anger': ['frustrated', 'angry', 'mad', 'hate', 'rage', 'furious'],

        'Excitement': ['excited', 'can’t wait', "can't wait", 'anticipation', 'journey', 'thrilled'],

    }

    

    for emotion, keywords in keyword_map.items():

        for kw in keywords:

            if kw in text_lower:

                emotions_found.add(emotion)

                break

                

    # Format exactly as user examples, e.g. "Joy + Anxiety"

    if emotions_found:

        # Let's ensure a specific ordering to match examples if possible

        ordered = []

        for e in ['Joy', 'Sadness', 'Fear', 'Anxiety', 'Anger', 'Excitement']:

            if e in emotions_found:

                ordered.append(e)

        return " + ".join(ordered) if ordered else " + ".join(list(emotions_found))

        

    # Fallback

    try:

        from textblob import TextBlob

        polarity = TextBlob(text).sentiment.polarity

        if polarity > 0.3:

            return "Joy"

        elif polarity < -0.3:

            return "Sadness"

        else:

            return "Neutral"

    except:

        return "Neutral"



@app.route('/')

def index():

    return render_template('index.html')



@app.route('/api/encrypt', methods=['POST'])

def encrypt_message():

    data = request.json

    text = data.get('text', '')

    

    if not text:

        return jsonify({"error": "No text provided"}), 400

        

    # 1. Detect Emotions

    emotion_result = extract_top_emotions(text)

    

    # 2. Encrypt Text

    key = Fernet.generate_key()

    f = Fernet(key)

    encrypted_text = f.encrypt(text.encode('utf-8')).decode('utf-8')

    

    # Store key for simplicity (in a real app, send it to user or store securely)

    # We will use the encrypted text itself as the reference ID

    keys_store[encrypted_text] = key

    

    # 3. Return payload (Encrypted Text + Visible Emotion)

    return jsonify({

        "encrypted_text": encrypted_text,

        "emotion": emotion_result,

        "key": key.decode('utf-8') # Returning key so frontend can use it for decryption

    })



@app.route('/api/decrypt', methods=['POST'])

def decrypt_message():

    data = request.json

    encrypted_text = data.get('encrypted_text', '')

    key = data.get('key', '').encode('utf-8')

    

    if not encrypted_text or not key:

        return jsonify({"error": "Encrypted text and key are required"}), 400

        

    try:

        # 1. Decrypt Text

        f = Fernet(key)

        decrypted_text = f.decrypt(encrypted_text.encode('utf-8')).decode('utf-8')

        

        # 2. Detect Emotion again just to show it still matches

        emotion_result = extract_top_emotions(decrypted_text)

        

        return jsonify({

            "decrypted_text": decrypted_text,

            "emotion": emotion_result

        })

    except Exception as e:

        return jsonify({"error": f"Decryption failed: {str(e)}"}), 400



if __name__ == '__main__':

    app.run(debug=True, port=5000)

