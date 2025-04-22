from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
import os


@CrewBase
class MentalHealthChatbotCrew:
    """MentalHealthChatbot crew"""
    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def emotion_detector(self) -> Agent:
        return Agent(config=self.agents_config["emotion_detector"])

    @agent
    def suggestion_agent(self) -> Agent:
        return Agent(config=self.agents_config["suggestion_agent"])

    @agent
    def safety_agent(self) -> Agent:
        return Agent(config=self.agents_config["safety_agent"])

    @agent
    def orchestrator(self) -> Agent:
        return Agent(config=self.agents_config["orchestrator"])

    @task
    def emotion_detection_task(self) -> Task:
        return Task(config=self.tasks_config["emotion_detection_task"],
                    output_file="logs/safety_check.md"
                    )

    @task
    def safety_check_task(self) -> Task:
        return Task(config=self.tasks_config["safety_check_task"],
                    output_file="logs/safety_check.md"
                    )

    @task
    def suggestion_task(self) -> Task:
        return Task(config=self.tasks_config["suggestion_task"],
                    output_file="logs/suggestion.md"
                    )

    @task
    def orchestrate_task(self) -> Task:
        return Task(config=self.tasks_config["orchestrate_task"],
                    output_file="logs/orchestrate.md"
                    )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )