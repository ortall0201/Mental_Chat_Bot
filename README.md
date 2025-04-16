# 🧠 Mental Chat Bot – CrewAI-Based POC

This repository contains the initial **Proof of Concept (POC)** for a modular, agentic mental health chatbot built using the **CrewAI framework**.

This POC includes only the **system structure and logical design**, with no real machine learning models, NLP pipelines, or datasets at this stage.

---

## 📌 Project Goal

To create a **multi-agent conversational AI** capable of supporting mental health users by detecting emotional states, providing self-help suggestions, and escalating high-risk situations — using an **agent-based architecture** powered by CrewAI.

This phase focuses on defining the core logic and agent orchestration.

---

## 🛠️ Framework: CrewAI

CrewAI enables the creation of multiple autonomous agents, each with a defined role and task, working collaboratively on a shared mission.

---

## 👥 Agents in the Initial POC

| Agent              | Description |
|-------------------|-------------|
| `EmotionDetector` | Analyzes user input and determines emotional state. |
| `SuggestionAgent` | Offers helpful suggestions based on the detected emotion. |
| `SafetyAgent`     | Assesses input for red flags or signs of crisis. |
| `RAGRetriever`    | Retrieves relevant knowledge or tips from a corpus. |
| `RAGReader`       | Summarizes and contextualizes retrieved knowledge. |

Each agent includes:
- A role  
- A goal  
- A backstory  
- Placeholder tools (mock logic only)

---

## 🧠 Memory Component

A simple user memory structure is used to simulate contextual awareness (e.g., storing the last detected emotion or suggestion). This will be extended in future development.

---

## 📂 Folder Structure

```
Mental_Chat_Bot/
├── agents/           # CrewAI agent definitions
├── tools/            # Placeholder logic for each agent
├── tasks/            # Task definitions and sequencing
├── memory/           # User memory logic (basic for now)
├── CrewAI_POC.ipynb  # Jupyter Notebook – main logic flow
├── run.py            # Optional script version of the flow
└── README.md         # Project documentation
```

---

## ✅ What's Implemented in This POC

- Defined 5 agents with backstories and goals  
- Created mock tool logic (no real ML/NLP yet)  
- CrewAI task flow orchestrated in notebook (`CrewAI_POC.ipynb`)  
- Memory placeholder added  
- System tested with one example input  

---

## 🧭 Next Steps (Post-POC Phase)

- Connect real NLP/ML models to each agent  
- Load and clean datasets (text + metadata)  
- Expand memory system  
- Deploy as a live demo or API  
- Add UI layer for user interaction

---

## 🤝 Team & Contributions

This project is developed collaboratively under the Omdena platform.  
To contribute, please refer to the [Task Tracker Sheet]([https://docs.google.com/spreadsheets/d/1vOj7uE34mnu577miQyK6Xf3lW1frFvfv2VAo_rTs1Vg/edit?gid=0#gid=0]) and assign yourself to an agent or module.

---

## 📬 Contact

Project lead: Ortal Lasry  
GitHub: [@ortall0201](https://github.com/ortall0201)
