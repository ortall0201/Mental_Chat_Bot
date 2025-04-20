# main.py

from crewai import Crew
from crew import agents, tasks
from langchain.memory import ConversationBufferMemory

print("\n🤖 Booting up the Mental Health Chatbot Crew...\n")

# Mock user input for testing
user_json = {
    "user_profile": {
        "name": "Alex",
        "age": 23,
        "gender": "non-binary",
        "occupation": "student",
        "marital_status": "single",
        "economic_status": "low",
        "mental_history": "Recent panic attacks, diagnosed with anxiety in the past."
    },
    "emotional_input": "I can't focus on anything anymore. I feel like I'm failing at life."
}

# Create a mock memory and inject user message
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
memory.chat_memory.add_user_message(
    f"Survey data: {user_json['user_profile']}\nUser said: {user_json['emotional_input']}"
)

# Define and run the crew
crew = Crew(
    agents=agents,
    tasks=tasks,
    verbose=True
)

# Run the workflow
final_output = crew.kickoff()

print("\n📝 Final Output:\n")
print(final_output)

# Safety alert logic
if "suicide" in final_output.lower() or "kill myself" in final_output.lower():
    print("\n⚠️  SAFETY ALERT: Contacting medical personnel or emergency contact...\n")
