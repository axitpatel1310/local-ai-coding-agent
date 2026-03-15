import json
import re
from agent.reasoning import ask_llm
from tools.file_tools import create_file, read_file, overwrite_file,append_file,delete_file,create_folder,delete_folder
from tools.execution_tools import run_python
from tools.file_tools import list_all,list_files,list_folders
TOOLS = {
    # File operations
    "create_file": create_file,
    "read_file": read_file,
    "overwrite_file": overwrite_file,
    "append_file": append_file,
    "delete_file": delete_file,

    # Folder operations
    "create_folder": create_folder,
    "delete_folder": delete_folder,

    # Listing
    "list_files": list_files,
    "list_folders": list_folders,
    "list_all": list_all,

    # Code execution
    "run_python": run_python
}

def extract_json(text):
    match = re.search(r'\{.*\}', text, re.DOTALL)
    if match:
        return match.group()
    else:
        raise Exception("No JSON found in model output")


class AgentController:

    def run(self, user_instruction):

        response = ask_llm(user_instruction)

        try:
            json_str = extract_json(response)
            action = json.loads(json_str)

            tool_name = action["tool"]
            args = action["args"]

            if tool_name in TOOLS:
                result = TOOLS[tool_name](**args)
                return result
            else:
                return "Unknown tool"

        except Exception as e:
            return f"Agent error: {str(e)}"