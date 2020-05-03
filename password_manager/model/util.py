"""
Module contains util functions

Created on Feb 27, 2020
@author: nenad.dramicanin
"""

from datetime import datetime
import pyperclip
import pathlib
import os
import sys

# Constant
__DATE_FORMAT = '%Y-%m-%d %H:%M:%S'


def get_current_date() -> str:
    """Returns current time in an appropriate format"""

    return datetime.today().strftime(__DATE_FORMAT)


def copy_to_clipboard(text: str):
    """Copies given text to clipboard"""

    pyperclip.copy(text)


def file_exists_and_not_empty(file_name: str) -> bool:
    """Checks whether provided file exists and it's not empty"""

    return pathlib.Path(file_name).is_file() and os.stat(file_name).st_size != 0


def get_root_path() -> str:
    """Returns application root path depending whether application is installed using 'Pyinstaller'
        or its running directly.

        In the case of Pyinstaller it's temp folder location will be returned, else two level up absolute path.
    """

    return sys._MEIPASS if getattr(sys, 'frozen', False) else \
        os.path.join(os.path.dirname(__file__), os.pardir, os.pardir)
