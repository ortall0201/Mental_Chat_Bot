from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
import yaml
from pathlib import Path
from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv

load_dotenv()

# Initialize LLM properly
llm = ChatOpenAI(
    model_name="gpt-4",
    temperature=0.8,
    model_kwargs={
        "top_p": 0.9,
        "frequency_penalty": 0.1,
        "presence_penalty": 0.1,
        "stop": ["END"]
    }
)

@CrewBase
class Mentalhealthbot():
    agents_config_path = Path(__file__).parent / 'config' / 'agents.yaml'
    tasks_config_path = Path(__file__).parent / 'config' / 'tasks.yaml'
    
    def __init__(self):
        super().__init__()  # Initialize CrewBase first
        
     
        try:
            with open(self.tasks_config_path) as f:
                self.tasks_config = yaml.safe_load(f) or {}
                
            with open(self.agents_config_path) as f:
                self.agents_config = yaml.safe_load(f) or {}
                # Clean agent configs
                for agent in self.agents_config.values():
                    if 'llm' in agent:
                        del agent['llm']
                        
        except Exception as e:
            raise RuntimeError(f"Config loading failed: {e}")
    # Agent Definitions
    @agent
    def emotion_analyser(self) -> Agent:
        return Agent(
            **self.agents_config['emotion_analyser'],
            llm=llm,
            verbose=True
        )

    @agent
    def knowledge_seeker(self) -> Agent:
        return Agent(
            **self.agents_config['knowledge_seeker'],
            llm=llm,
            verbose=True
        )

    @agent
    def suggestion_provider(self) -> Agent:
        return Agent(
            **self.agents_config['suggestion_provider'],
            llm=llm,
            verbose=True
        )

    # Task Definitions
    @task
    def analyse_emotion(self) -> Task:
        return Task(
            **self.tasks_config['analyse_emotion'],
            agent=self.emotion_analyser()
        )

    @task
    def retrieve_resources(self) -> Task:
        return Task(
            **self.tasks_config['retrieve_resources'],
            agent=self.knowledge_seeker()
        )

    @task
    def generate_response(self) -> Task:
        return Task(
            **self.tasks_config['generate_response'],
            agent=self.suggestion_provider()
        )
    
    @crew
    def crew(self) -> Crew:
        """Creates the Mentalhealthbot crew"""
        return Crew(
            agents=[
                self.emotion_analyser(),
                self.knowledge_seeker(),
                self.suggestion_provider()
            ],
            tasks=[
                self.analyse_emotion(),
                self.retrieve_resources(),
                self.generate_response()
            ],
            process=Process.sequential,
            verbose=2
        )
