#!/usr/bin/env python
import sys
import warnings
import os
from datetime import datetime
from dotenv import load_dotenv  # << Required to load your .env file

from ortal_crewai.crew import MentalHealthCrew

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# 🔁 Load .env so OPENAI_API_KEY gets picked up
load_dotenv()

def run():
    inputs = {
        'topic': 'AI LLMs',
        'current_year': str(datetime.now().year)
    }
    try:
        MentalHealthCrew().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")
