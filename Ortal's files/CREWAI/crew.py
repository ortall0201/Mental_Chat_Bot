# crew.py

from crewai import Agent, Task
from langchain_community.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Set up the LLM
llm = ChatOpenAI(
    model_name="gpt-3.5-turbo",
    temperature=0.6,
    openai_api_key=os.getenv("OPENAI_API_KEY")
)

# Shared memory for context between agents
shared_memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

# Agent 0: Safety Checker Agent
safety_agent = Agent(
    role="Safety Monitor",
    goal="Scan input for signs of suicidal ideation or abuse and raise an alert if necessary.",
    backstory="You ensure the safety of the user. If any red flags (self-harm, violence, abuse) are detected, you notify the proper contact or authority.",
    verbose=True,
    memory=shared_memory,
    llm=llm
)

# Agent 1: Cloud Data Fetcher for Layer 1 (User Survey + Emotion CSV)
cloud_emotion_data_agent = Agent(
    role="Emotion Data Fetcher",
    goal="Fetch user survey data and preprocessed binary emotion datasets from cloud storage.",
    backstory="You are responsible for retrieving the user's context (age, gender, occupation, etc.) and structured emotion-labeled training data.",
    verbose=True,
    memory=shared_memory,
    llm=llm
)

# Agent 2: Intake Agent
intake_agent = Agent(
    role="Intake Agent",
    goal="Collect user's emotional experience in their own words.",
    backstory="You're a supportive entry point for users to express their emotional state. You integrate structured survey data with open-text input.",
    verbose=True,
    memory=shared_memory,
    llm=llm
)

# Agent 3: Emotion Classifier
emotion_classifier = Agent(
    role="Emotion Classifier",
    goal="Classify the user's primary emotional state using both text and binary emotion datasets.",
    backstory="You apply emotional recognition based on training data and recent user input.",
    verbose=True,
    memory=shared_memory,
    llm=llm
)

# Agent 4: Cloud Data Fetcher for Layer 2 (Solutions Knowledge Base)
cloud_solution_data_agent = Agent(
    role="Solution Dataset Fetcher",
    goal="Retrieve online knowledge (PDFs, HTMLs) for exercises, articles, and coping strategies.",
    backstory="You serve relevant documents for RAG-based support based on the user's detected emotion.",
    verbose=True,
    memory=shared_memory,
    llm=llm
)

# Agent 5: Solution Advisor
solution_advisor = Agent(
    role="Solution Advisor",
    goal="Suggest personalized coping strategies based on emotion and context.",
    backstory="You analyze emotion types and fetch relevant RAG documents to generate non-clinical support suggestions.",
    verbose=True,
    memory=shared_memory,
    llm=llm
)

# Agent 6: Support Generator
support_agent = Agent(
    role="Support Generator",
    goal="Craft an empathetic final message that includes emotional validation and a solution.",
    backstory="You synthesize all inputs to give the user a calm, affirming message with one actionable step or resource.",
    verbose=True,
    memory=shared_memory,
    llm=llm
)

# Tasks
safety_task = Task(
    description="Scan the user's emotional input for suicidal thoughts or abuse. If found, prepare a flag message.",
    expected_output="Safety alert or clearance",
    agent=safety_agent
)

fetch_emotion_data = Task(
    description="Load the user's structured survey info and preprocessed emotion dataset from the cloud.",
    expected_output="User profile + binary-labeled emotion dataset",
    agent=cloud_emotion_data_agent
)

intake_task = Task(
    description="Ask the user how they are feeling and combine their free-text response with survey data.",
    expected_output="A short emotional description + structured profile",
    agent=intake_agent
)

classify_task = Task(
    description="Use binary emotion data and user input to classify emotional state.",
    expected_output="The dominant emotion with brief justification",
    agent=emotion_classifier
)

fetch_solutions_task = Task(
    description="Retrieve relevant documents from PDFs and HTMLs based on detected emotion.",
    expected_output="Set of emotional support documents",
    agent=cloud_solution_data_agent
)

solution_task = Task(
    description="Match emotion to a solution from the RAG-based resources.",
    expected_output="Selected exercise, coping strategy, or resource",
    agent=solution_advisor
)

support_task = Task(
    description="Generate a kind, encouraging final message to the user that includes validation and a solution.",
    expected_output="Final user-facing message",
    agent=support_agent
)

# Export agents and tasks
agents = [
    safety_agent,
    cloud_emotion_data_agent,
    intake_agent,
    emotion_classifier,
    cloud_solution_data_agent,
    solution_advisor,
    support_agent
]

tasks = [
    safety_task,
    fetch_emotion_data,
    intake_task,
    classify_task,
    fetch_solutions_task,
    solution_task,
    support_task
]
