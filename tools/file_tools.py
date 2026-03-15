import os
from security.safe_path import safe_path

WORKSPACE = "workspace"


# Ensure workspace exists
os.makedirs(WORKSPACE, exist_ok=True)


# ----------------------
# FILE OPERATIONS
# ----------------------

def create_file(filename, content):
    path = safe_path(os.path.join(WORKSPACE, filename))
    content = content.replace("\\n", "\n")
    with open(path, "w") as f:
        f.write(content)
    return f"File {filename} created."

def read_file(filename):
    path = safe_path(os.path.join(WORKSPACE, filename))
    with open(path, "r") as f:
        return f.read()


def overwrite_file(filename, content):
    path = safe_path(os.path.join(WORKSPACE, filename))

    with open(path, "w") as f:
        f.write(content)

    return f"File '{filename}' overwritten."


def append_file(filename, content):
    path = safe_path(os.path.join(WORKSPACE, filename))

    with open(path, "a") as f:
        f.write(content)

    return f"Content appended to '{filename}'."


def delete_file(filename):
    path = safe_path(os.path.join(WORKSPACE, filename))

    if os.path.exists(path):
        os.remove(path)
        return f"File '{filename}' deleted."

    return "File not found."


# ----------------------
# FOLDER OPERATIONS
# ----------------------

def create_folder(foldername):
    path = safe_path(os.path.join(WORKSPACE, foldername))

    os.makedirs(path, exist_ok=True)

    return f"Folder '{foldername}' created."


def delete_folder(foldername):
    path = safe_path(os.path.join(WORKSPACE, foldername))

    if os.path.exists(path):
        os.rmdir(path)
        return f"Folder '{foldername}' deleted."

    return "Folder not found."


# ----------------------
# LIST OPERATIONS
# ----------------------

def list_files():
    path = safe_path(WORKSPACE)

    return [
        f for f in os.listdir(path)
        if os.path.isfile(os.path.join(path, f))
    ]


def list_folders():
    path = safe_path(WORKSPACE)

    return [
        f for f in os.listdir(path)
        if os.path.isdir(os.path.join(path, f))
    ]


def list_all():
    path = safe_path(WORKSPACE)

    return os.listdir(path)