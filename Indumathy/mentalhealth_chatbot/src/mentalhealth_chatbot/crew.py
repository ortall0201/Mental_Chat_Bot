from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from mentalhealth_chatbot.tools.custom_tool import EmotionAnalysisTool, SafetyCheckTool


@CrewBase
class MentalHealthCrew():
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'
    
    @agent
    def emotion_detector(self) -> Agent:
        return Agent(
            config=self.agents_config['emotion_detector'],
            tools=[EmotionAnalysisTool()],
            verbose=True
        )

    @agent
    def suggestion_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['suggestion_agent'],
            tools=[SafetyCheckTool()],
            verbose=True
        )

    @task
    def detect_emotion(self) -> Task:
        return Task(
            config=self.tasks_config['detect_emotion'],
            agent=self.emotion_detector(),
            output_file='outputs/emotion.md',
            expected_output="{'emotion': 'detected_emotion'}"
        )

    @task
    def provide_suggestions(self) -> Task:
        return Task(
            config=self.tasks_config['provide_suggestions'],
            agent=self.suggestion_agent(),
            output_file='outputs/suggestions.md',
            context=[self.detect_emotion()]  # Proper task chaining
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=[self.detect_emotion(), self.provide_suggestions()],
            process=Process.sequential,
            verbose=True,
            memory=False  # Disable memory to prevent looping
        )