import sys
import os
sys.path.append(os.path.abspath("src"))

import streamlit as st
from dotenv import load_dotenv
from mentalhealth_chatbot.main import get_bot_response

# Load environment variables
load_dotenv()

# Page setup
st.set_page_config(page_title="Mental Health Chatbot", page_icon="🤖")
st.title("🤖 Mental Health Chatbot")

# API Key check
if not os.getenv("GOOGLE_API_KEY"):
    st.warning("Please set your GOOGLE_API_KEY in a .env file before using the chatbot.")
    st.stop()

# Initialize conversation
if "conversation" not in st.session_state:
    st.session_state.conversation = []

# Static welcome prompt
st.markdown("### How are you feeling today?")

# Show chat history
for msg in st.session_state.conversation:
    if msg.startswith("User:"):
        st.markdown(f"🧑 **You:** {msg[6:]}")
    elif msg.startswith("Bot:"):
        st.markdown(f"🤖 **Bot:** {msg[5:]}")

# Custom styling for clean input + send button
st.markdown("""
    <style>
    div[data-baseweb="input"] input {
        padding: 10px;
        border-radius: 8px;
        border: 1px solid #ccc;
    }
    button[kind="formSubmit"] {
        width: 42px;
        height: 42px;
        border-radius: 8px;
        margin-top: 0px;
    }
    </style>
""", unsafe_allow_html=True)

# Input row with icon
with st.form(key="chat_form", clear_on_submit=True):
    cols = st.columns([10, 1])
    user_input = cols[0].text_input(
        "", 
        placeholder="Type your message...", 
        label_visibility="collapsed"
    )
    submitted = cols[1].form_submit_button("➤")

# On message send
if submitted and user_input:
    conversation_history = st.session_state.conversation.copy()

    with st.spinner("Thinking..."):
        bot_reply, updated_convo = get_bot_response(user_input, conversation_history)
        st.session_state.conversation = updated_convo

    st.rerun()
