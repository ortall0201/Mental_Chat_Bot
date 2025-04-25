#!/usr/bin/env python
import sys
import warnings
import os
from datetime import datetime
from dotenv import load_dotenv 
from my_project.crew import MyProject

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")
load_dotenv()

def run():
    inputs = {
        'topic': 'AI LLMs',
        'current_year': str(datetime.now().year)
    }
    try:
        MyProject().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")
