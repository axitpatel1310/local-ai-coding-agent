import subprocess
import os
from security.safe_path import safe_path

WORKSPACE = "workspace"


def run_python(file):

    path = safe_path(os.path.join(WORKSPACE, file))

    result = subprocess.run(
        ["python", path],
        capture_output=True,
        text=True
    )

    return {
        "stdout": result.stdout,
        "stderr": result.stderr
    }