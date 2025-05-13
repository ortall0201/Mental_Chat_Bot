
from src.mental_health_chat_bot.crew import MentalHealthChatbotCrew
from dotenv import load_dotenv
import datetime

import sys
import os

#project's root to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

#import speech recognizer (for STT)
from speech_to_text import recognize_speech_from_mic


# Load environment variables
load_dotenv()
# print("GOOGLE_API_KEY:", os.getenv("GOOGLE_API_KEY"))  # Debug print

#added def for STT
def capture_user_input():
    """Captures user input from mic and returns text."""
    user_input = recognize_speech_from_mic()
    return user_input

def log_conversation(message: str):
    """Append message to conversation log with timestamp."""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("logs/conversation_log.txt", "a") as f:
        f.write(f"[{timestamp}] {message}\n")

def main():
    print("Welcome to the Mental Health Chatbot. I'm here to listen and support you.")
    print("Type 'exit' to end the conversation.\n")
    log_conversation("Chatbot started.")

    conversation_history = []
    while True:
        ##STT -code block- starts to input
        user_input = capture_user_input()  # <-- USE MICROPHONE NOW

        if not user_input:
            print("Didn't catch that. Try speaking again.")
            continue
        ###STT -code block- ends

        log_conversation(f"You: {user_input}")

        if user_input.lower() == "exit":
            print("Goodbye. Take care!")
            log_conversation("Chatbot ended.")
            break

        conversation_history.append(f"User: {user_input}")
        inputs = {
            "user_input": user_input,
            "conversation_history": "\n".join(conversation_history[-5:])
        }

        crew = MentalHealthChatbotCrew()
        result = crew.crew().kickoff(inputs=inputs)

        conversation_history.append(f"Bot: {result}")
        print(f"Bot: {result}\n")
        log_conversation(f"Bot: {result}")

if __name__ == "__main__":
    main()