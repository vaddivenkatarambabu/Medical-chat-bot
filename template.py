import os
import pathlib
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]:%(message)s:')

list_of_files = [
    "scr/__init__.py",
    "scr/helper.py",
    "scr/prompt.py",
    ".env",
    "setup.py",
    "research/trials.ipynb"
    "test.py"
]

for filepath in list_of_files:
    filepath = pathlib.Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory {filepath} for the file {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
        logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"File {filepath} already exists")