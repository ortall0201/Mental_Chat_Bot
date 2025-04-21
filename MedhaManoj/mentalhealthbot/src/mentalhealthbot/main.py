

from mentalhealthbot.crew import Mentalhealthbot

if __name__ == "__main__":
    bot = Mentalhealthbot()
    user_input = input("💬 How are you feeling today?\n> ")
    result = bot.crew().kickoff(inputs={
        "input": user_input
    })
    print(result)