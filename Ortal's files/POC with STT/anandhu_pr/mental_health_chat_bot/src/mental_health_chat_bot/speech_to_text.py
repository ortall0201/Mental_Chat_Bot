import speech_recognition as sr
import os
from dotenv import load_dotenv

load_dotenv()

def recognize_speech_from_mic():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        print("🎤 Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("🧠 Recognizing speech...")
        # No need to pass credentials manually
        text = recognizer.recognize_google_cloud(audio)
        print(f"📝 Recognized: {text}")
        return text
    except Exception as e:
        print(f"❗ Error recognizing speech: {e}")
        return None
