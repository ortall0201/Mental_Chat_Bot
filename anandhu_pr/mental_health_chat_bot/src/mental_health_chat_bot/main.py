
from src.mental_health_chat_bot.crew import MentalHealthChatbotCrew
from dotenv import load_dotenv
import os


def main():
    print("Welcome to the Mental Health Chatbot. I'm here to listen and support you.")
    print("Type 'exit' to end the conversation.\n")

    conversation_history = []
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Goodbye. Take care!")
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

if __name__ == "__main__":
    main()