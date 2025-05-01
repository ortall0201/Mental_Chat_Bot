import sys
import os
from datetime import datetime
import streamlit as st
from dotenv import load_dotenv
load_dotenv()
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))
from my_project.crew import MyProject

# title
st.set_page_config(page_title="Mental Health Chatbot", layout="centered")
st.title("🧠 Mental Health Support Chatbot")

# Initialize session state
if 'conversation' not in st.session_state:
    st.session_state.conversation = []

# conversation history
for entry in st.session_state.conversation:
    if entry['role'] == 'User':
        st.markdown(f"**You:** {entry['message']}")
    else:
        st.markdown(f"**Bot:** {entry['message']}")

with st.form(key="chat_form", clear_on_submit=True):
    user_input = st.text_area("What's on your mind?", height=150, key="input_area")
    submitted = st.form_submit_button("Send")

if submitted and user_input.strip() != "":
    st.session_state.conversation.append({'role': 'User', 'message': user_input})
    inputs = {
        'topic': user_input,
        'current_year': str(datetime.now().year)
    }

    try:
        result = MyProject().crew().kickoff(inputs=inputs)
        st.session_state.conversation.append({'role': 'Bot', 'message': result})

    except Exception as e:
        st.error(f"Error: {str(e)}")
