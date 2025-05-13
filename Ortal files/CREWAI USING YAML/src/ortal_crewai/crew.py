from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

@CrewBase
class MentalHealthCrew():
    """Mental Health Chatbot Crew"""

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def orchestrator(self) -> Agent:
        return Agent(
            config=self.agents_config['orchestrator'],
            verbose=True
        )

    @agent
    def emotion_classifier(self) -> Agent:
        return Agent(
            config=self.agents_config['emotion_classifier'],
            verbose=True
        )

    @agent
    def knowledge_reader(self) -> Agent:
        return Agent(
            config=self.agents_config['knowledge_reader'],
            verbose=True
        )

    @agent
    def knowledge_retriever(self) -> Agent:
        return Agent(
            config=self.agents_config['knowledge_retriever'],
            verbose=True
        )

    @agent
    def solution_synthesizer(self) -> Agent:
        return Agent(
            config=self.agents_config['solution_synthesizer'],
            verbose=True
        )

    @task
    def plan_flow(self) -> Task:
        return Task(
            config=self.tasks_config['plan_flow']
        )

    @task
    def classify_emotion(self) -> Task:
        return Task(
            config=self.tasks_config['classify_emotion']
        )

    @task
    def read_knowledge(self) -> Task:
        return Task(
            config=self.tasks_config['read_knowledge']
        )

    @task
    def retrieve_knowledge(self) -> Task:
        return Task(
            config=self.tasks_config['retrieve_knowledge']
        )

    @task
    def compose_response(self) -> Task:
        return Task(
            config=self.tasks_config['compose_response']
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True
        )
