🤖 AI-Powered Code Reviewer & Quality Assistant

An intelligent Python code analysis tool that automatically reviews code quality, detects issues, generates docstrings, calculates scores, and provides AI-powered improvement suggestions.

🚀 Features

Static code analysis (functions, classes, imports)

Quality scoring system

Automatic docstring generation

Issue detection & reporting

CSV report export

AI-powered suggestions using LLM

Auto code improvement feature

Interactive Streamlit dashboard

🧠 How It Works

Pipeline:

Parser → Analyzer → Metrics → Validator → LLM → UI Dashboard

Parser extracts structure from Python file

Analyzer detects code issues

Metrics calculates quality score

Validator checks docstring quality

LLM suggests improvements

UI displays results interactively

📦 Installation

Clone repository:

git clone https://github.com/Rishitha-32/ai-code-reviewer.git
cd ai-code-reviewer

Install dependencies:

pip install -r requirements.txt
🔑 Environment Setup

Set API key:

setx OPENAI_API_KEY "your_api_key_here"

Restart terminal after setting.

▶ Run Application
python -m streamlit run ui/app.py

Open browser:

http://localhost:8501
📊 Example Output

Dashboard shows:

Function metrics

Code quality scores

Issues detected

AI suggestions

Improved code output

🛠 Tech Stack

Python

AST Parsing

Streamlit

OpenAI API

Pandas

🎯 Use Cases

Code review automation

Student code evaluation

Developer productivity tool

Pre-commit quality checks

CI/CD integration

📁 Project Structure
ai-code-reviewer/
│
├── core/
│   ├── parser.py
│   ├── analyzer.py
│   ├── validator.py
│   ├── metrics.py
│   └── llm_reviewer.py
│
├── ui/
│   └── app.py
│
└── README.md
👩‍💻 Author

Rishitha R
GitHub: https://github.com/Rishitha-32

⭐ Future Improvements

Multi-language support

GitHub PR integration

Auto formatting fixes

Code smell detection

Team review analytics

📜 License

This project is open-source and free for educational purposes.

✅ Next Step — Upload README
