# 🧠 From Prompt to Action — AI Agent Project

This repository ports the Kaggle notebook **“Day 1a – From Prompt to Action”** from the *5 Days of AI Agents* series into a fully reproducible and extensible GitHub project.

The goal is to build and explore an **AI Agent** that can take natural-language instructions and autonomously perform actions or generate structured results using the **Google AI Development Kit (ADK)** and **Gemini API**.

---

## 🚀 Overview

This project is the foundation of an intelligent system that turns text prompts into executable actions.

It demonstrates how to:
- Set up the **Google AI Development Kit (ADK)**.
- Build your **first AI Agent** capable of interpreting human language.
- Interact with the **ADK Web Interface** for visualization.
- Extend the agent to handle multi-step reasoning and richer outputs.

---

## 🧩 Project Structure

```
.
├── notebook.ipynb    # Original Kaggle notebook
├── src/
│   ├── agent.py                             # Core agent implementation
│   ├── utils.py                             # Helper functions for logging, prompts, etc.
│   └── __init__.py
├── requirements.txt                         # Dependencies
├── .gitignore
└── README.md
```

---

## ⚙️ Setup

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Configure environment variables
Set your **Gemini API key**:
```bash
export GEMINI_API_KEY="your_api_key_here"
```

---

## 📓 Usage

You can run this project either via **Jupyter Notebook** or as a **Python module**.

### Option A — Run the Notebook
```bash
jupyter lab notebook.ipynb
```

### Option B — Run the Agent Script
```bash
python src/agent.py
```

---

## 🧠 What the Agent Does

The AI Agent:
1. Accepts a natural-language instruction (e.g., “Summarize this paragraph”).
2. Uses the Gemini model through ADK to understand intent.
3. Generates executable actions or responses.
4. Displays structured or visualized outputs interactively.

Example:
```python
agent.run("Create a short poem about AI Agents learning from humans.")
```

---

## 🧪 Extend the Project

Future ideas:
- 🧰 Add memory or context chaining for multi-step reasoning.
- 🔗 Integrate external tools (search, data APIs, or code execution).
- 🎨 Build a web interface to interact with your agent visually.
- 🧩 Convert this into a modular `pip` package for easy reuse.

---

## 🧑‍💻 For GitHub Copilot

When suggesting code:
- Focus on **extensibility** and **clarity**.
- Keep examples **educational** for beginners exploring ADK and agents.
- Use clear function docstrings and type hints.
- Suggest improvements for modularity and testability.

---

## 💬 Acknowledgements

Based on the Kaggle course:
> *5 Days of AI Agents with Google*  
> Original Notebook: [Day 1a - From Prompt to Action](https://www.kaggle.com/code/kaggle5daysofai/day-1a-from-prompt-to-action)

---
