import os

WORKSPACE = os.path.abspath("workspace")


def safe_path(path):

    absolute = os.path.abspath(path)

    if not absolute.startswith(WORKSPACE):
        raise Exception("Access outside workspace blocked")

    return absolute