# EmotionAwarness 🎭🔒

A simple but trippy experiment: what if we could encrypt the content of a message, but *keep the emotional sentiment readable* for AI agents or bots? 

I built this over the weekend as a proof-of-concept for secure, privacy-preserving sentiment analysis. Basically, if you type something like "I am so incredibly happy, joyful, and excited right now!", the app encrypts the actual text into total garbage. *But*, it correctly extracts and exposes a tag like `Joy` alongside the payload.

If you hit decrypt, you get the original message back. 

### How it works 🛠️

It's a pretty straightforward stack:
* **Backend:** Flask API handling the heavy lifting.
* **Encryption:** Symmetric Fernet encryption via the `cryptography` lib. The key is managed in memory right now since it's just a demo.
* **Emotion Analysis:** I patched together a custom keyword mapping layered on top of TextBlob to handle complex, multi-emotion strings. It can actually detect combinations like `Joy + Anxiety` or `Sadness + Anger` pretty accurately.
* **Frontend:** Built a slick glassmorphism UI with Vanilla HTML/JS/CSS. No heavy frameworks, just clean API calls.

### Quick Start 🚀

1. Clone it down.
2. Run the batch script to install stuff and download the NLTK corpuses:
   ```cmd
   setup.bat
   ```
3. Alternatively, do it manually:
    ```bash
    pip install -r requirements.txt
    python -m textblob.download_corpora
    python app.py
    ```
4. Open `http://127.0.0.1:5000/` and start encrypting your feelings.

### Why build this?
Data privacy is obviously huge right now, and the idea of "semantic encryption" is fascinating. What if a moderation AI could flag a message as `Anger` without actually violating the user's end-to-end encrypted text? This is a super basic step toward that concept.

Feel free to fork it, break it, or use the UI for something else. 

---
*Tested specifically on complex multi-emotion sentences, so throw your mixed feelings at it.*
