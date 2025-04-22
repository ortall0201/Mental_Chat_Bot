from mentalhealth_chatbot.crew import MentalHealthCrew

def run():
    print("Mental Health Chatbot")
    print("---------------------")
    
    while True:
        user_input = input("\nHow are you feeling today? (type 'quit' to exit): ").strip()
        if user_input.lower() in ['quit', 'exit']:
            break
            
        # Provide ALL required variables
        result = MentalHealthCrew().crew().kickoff(inputs={
            'user_input': user_input
            
        })
        
        print("\n=== Suggestions ===")
        print(result)