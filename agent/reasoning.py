import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "qwen2.5:3b-instruct"

SYSTEM_PROMPT = """
You are an autonomous coding agent.

Your job is to complete programming tasks fully.

You can use tools to interact with the environment.

IMPORTANT RULES:

1. If the user asks to create code, you must write runnable code.
2. Python scripts must produce visible output using print().
3. After creating a Python file, the next step should usually be to run it.
4. Only return ONE JSON tool call.

5. When writing code:
- Write real code with normal line breaks.
- Do NOT escape newlines using \\n.
- Write clean Python scripts.

Output format:

{
 "tool": "tool_name",
 "args": {}
}

Available tools:

File operations:
create_file(filename, content)
read_file(filename)
overwrite_file(filename, content)
append_file(filename, content)
delete_file(filename)

Folder operations:
create_folder(foldername)
delete_folder(foldername)

Listing operations:
list_files()
list_folders()
list_all()

Execution:
run_python(file)

Workspace rules:
- All files are inside workspace/
- Python scripts should include example usage and print results.
"""


def ask_llm(user_input):

    prompt = SYSTEM_PROMPT + "\nUser request: " + user_input

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL,
            "prompt": prompt,
            "stream": False
        }
    )

    return response.json()["response"]