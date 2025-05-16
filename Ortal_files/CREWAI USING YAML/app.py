# FILE: gradio_app.py
import gradio as gr
from ortal_crewai.crew import MentalHealthCrew

def run_chat(user_input):
    inputs = {
        'topic': user_input,
        'current_year': '2025'
    }
    try:
        result = MentalHealthCrew().crew().kickoff(inputs=inputs)
        return str(result)
    except Exception as e:
        return f"Error: {str(e)}"

# Simple Gradio UI
iface = gr.Interface(
    fn=run_chat,
    inputs=gr.Textbox(label="What's on your mind?"),
    outputs="text",
)

# 👇 This line launches the app in your browser
iface.launch()
