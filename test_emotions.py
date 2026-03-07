from nrclex import NRCLex

def test(text):
    print(f"\n--- Testing: {text}")
    try:
        obj = NRCLex(text)
        if hasattr(obj, 'raw_emotion_scores'):
            print("Raw scores:", obj.raw_emotion_scores)
        if hasattr(obj, 'top_emotions'):
            print("Top emotions:", obj.top_emotions)
        if hasattr(obj, 'affect_dict'):
            print("Affect dict:", obj.affect_dict)
            
    except Exception as e:
        print("Error:", e)

test("Feeling ecstatic about joining the new AI research team, though a bit anxious about the deadlines ahead.")
test("I can’t believe I failed that test again. I’m so disappointed and frustrated right now.")
test("Finally got the job offer! I’m thrilled and can’t wait to start this new journey.")
