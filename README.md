# Local Coding Agent

A **local autonomous coding agent** that converts natural language instructions into actions on a codebase.

The agent uses a **Large Language Model (via Ollama)** to reason about programming tasks and execute them using tools such as file manipulation, code execution, and project navigation.

This project demonstrates the core architecture behind modern coding agents such as **Cursor, Devin, and OpenDevin**.

---

# Architecture

The system follows the **ReAct (Reason → Act → Observe)** pattern.

User Instruction  
↓  
LLM Reasoning  
↓  
Tool Selection  
↓  
Tool Execution  
↓  
Result Returned  
↓  
Next Decision

Core definition:

Coding Agent = LLM + Tool System + Execution Loop + Memory

---

# Features

### Natural Language Programming

Example:

User:  

write a simple linear regression in machine.py


The agent can:

• create the file  
• write Python code  
• execute the program  
• return the output  

---

### File System Manipulation

The agent can interact with files inside a secure workspace.

Supported operations:

- create_file
- read_file
- overwrite_file
- delete_file

---

### Code Execution

Python scripts can be executed automatically.

Output includes:

- stdout
- stderr
- runtime errors

This enables **automatic debugging workflows**.

---

### Workspace Sandbox

All generated code runs inside a dedicated directory:


workspace/


Security layer prevents access outside the workspace.

Example blocked path:


../../etc/passwd


---

# Project Structure


coding-agent/
│
├── main.py
│
├── agent/
│ ├── controller.py
│ └── reasoning.py
│
├── tools/
│ ├── file_tools.py
│ └── execution_tools.py
│
├── security/
│ └── safe_path.py
│
└── workspace/


---

# How It Works

### 1. User Request

Example:


write a python script that prints hello world


---

### 2. LLM Reasoning

The model decides which tool to call.

Example output:


{
"tool": "create_file",
"args": {
"filename": "hello.py",
"content": "print('Hello world')"
}
}


---

### 3. Tool Execution

The agent executes the selected tool.

Example:


create_file("hello.py")


---

### 4. Program Execution


run_python("hello.py")


Output:


Hello world


---

# Setup

## 1 Install Dependencies


pip install -r requirements.txt


---

## 2 Install Ollama

https://ollama.com

Start a coding model:


ollama run codellama


or


ollama run deepseek-coder


---

## 3 Run the Agent


python main.py


---

# Example Interaction


User: create a python file that prints hello

Agent: File hello.py created

User: run hello.py

Agent:
stdout: Hello


---

# Limitations

Current version is a **Level-1 coding agent**.

Limitations:

- Single-step reasoning
- No semantic code search
- No AST-based editing
- No multi-agent planning
- Limited memory

---

# Future Improvements

Planned upgrades:

- Vector-based code search
- Multi-step execution loop
- Auto debugging
- Planner agent
- AST-based code editing
- Repository indexing

These upgrades move the system toward a **fully autonomous coding assistant**.

---

# Tech Stack

Python  
Ollama  
Local LLM (CodeLlama / DeepSeek Coder)

---

# Inspiration

The architecture is inspired by:

- Cursor
- Devin
- OpenDevin
- LangChain Agents
- ReAct pattern

