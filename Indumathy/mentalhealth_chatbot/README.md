# 🧠 Omdena MindfulChat – Mental Health Chatbot (Team 1)

This is a voice-enabled, agentic AI-based mental health chatbot developed using **CrewAI**, **FastAPI**, and **React**. It provides users with personalized self-care suggestions, multi-step mental health assessments, and voice/text interactions, supported by Retrieval-Augmented Generation (RAG).

---

## 🚀 Features

- ✨ **CrewAI Multi-Agent Architecture**: EmotionDetector, SuggestionAgent, SafetyAgent, RAGRetriever, RAGReader
- 🔍 **RAG Search**: Uses HuggingFace embeddings and FAISS vector database for tip retrieval
- 🧠 **LLM Integration**: Gemini 2.0 Flash via API key (no Google Cloud required)
- 🗣️ **Voice Interaction**:
  - **STT**: Whisper for speech-to-text
  - **TTS**: pyttsx3 for local text-to-speech
- 🧪 **Assessments**: Multi-step mental health surveys (Stress, Anxiety, Depression, FOMO)
- 💾 **Session Memory**: Tracks user inputs and stores logs in CSV format

---

## 🧰 Tech Stack

- **Frontend**: React + TailwindCSS  
- **Backend**: FastAPI (Python)
- **LLM**: Gemini (API key-based)
- **Embeddings**: HuggingFace (MiniLM-L6-v2)
- **Vector DB**: FAISS
- **Voice Tools**: Whisper (STT), pyttsx3 (TTS)
- **Agents**: CrewAI with YAML config
- **Memory**: CSV-based logs for sessions and assessments

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/OmdenaAI/agentic-based-Mental-Health-chatbot-using-Langchain-workflows.git
cd agentic-based-Mental-Health-chatbot-using-Langchain-workflows
git checkout team1
cd POC_UI_STT_TTS_10_5

### 2️⃣ Backend Setup (FastAPI)
python -m venv venv
venv\Scripts\activate          # On Windows
cd mentalhealth_chatbot
pip install .       # To run pyproject.toml

### Create .env file inside mentalhealth_chatbot
GEMINI_API_KEY=your_gemini_api_key_here
## Run the backend
uvicorn fastapi_app.main:app --reload

### 3️⃣ Frontend Setup (React)
## Go to new terminal
cd POC_UI_STT_TTS_10_5/frontend
npm install
npm start


### Then open below link  in the browser
http://localhost:3000
