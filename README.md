# 5-day-agents-from-prompt-to-action
Your First AI Agent: From Prompt to Action

## 🎯 Overview
This project demonstrates how to build an **AI Agent** that can understand natural-language instructions and perform actions autonomously using Google's Gemini API and the Google ADK.

## 🧩 Project Structure
- `notebook.ipynb` — main notebook migrated from Kaggle with examples and tutorials
- `src/agent.py` — reusable agent logic using `google-adk` and `Gemini API`
- `requirements.txt` — includes `google-adk`, `google-generativeai`, and helper libs

## ⚙️ Setup

### Prerequisites
- Python 3.8 or higher
- Google API key (get one from [Google AI Studio](https://makersuite.google.com/app/apikey))

### Installation

1. Clone the repository:
```bash
git clone https://github.com/jdnichollsc/5-day-agents-from-prompt-to-action.git
cd 5-day-agents-from-prompt-to-action
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

Or install manually:
```bash
pip install google-adk google-generativeai jupyterlab
```

3. Set up your API key:
Create a `.env` file in the project root:
```bash
GOOGLE_API_KEY=your-api-key-here
```

## 🚀 Usage

### Using the Jupyter Notebook
Launch JupyterLab and open `notebook.ipynb`:
```bash
jupyter lab
```

### Using the Agent Programmatically
```python
from src.agent import create_agent

# Create an agent instance
agent = create_agent()

# Generate content
response = agent.generate_content("Explain quantum computing in simple terms")
print(response)

# Start a chat session
agent.start_chat()
response = agent.send_message("Hello! Can you help me with Python?")
print(response)
```

## 📚 Features
- **Natural Language Understanding**: Process and respond to natural language instructions
- **Chat Sessions**: Maintain conversation context across multiple interactions
- **Content Generation**: Generate content based on prompts
- **Chat History**: Access and review conversation history
- **Extensible Design**: Easy to customize and extend for specific use cases

## 🛠️ Development
The agent is built using:
- **Google ADK**: For agent development kit functionality
- **Google Generative AI**: For accessing the Gemini API
- **Python-dotenv**: For environment variable management

## 📖 Examples
Check out `notebook.ipynb` for comprehensive examples including:
- Simple content generation
- Interactive chat sessions
- Task-oriented agents
- Code generation
- Chat history management

## 🤝 Contributing
Contributions are welcome! Feel free to open issues or submit pull requests.

## 📄 License
See [LICENSE](LICENSE) for details.
