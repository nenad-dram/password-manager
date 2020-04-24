'''
Created on Feb 27, 2020

@author: ndramica
'''
from datetime import datetime
import pyperclip

from pathlib import Path
import os


def get_current_date():
    return datetime.today().strftime('%Y-%m-%d %H:%M:%S')


def copy_to_clipboard(text):
    pyperclip.copy(text)


def file_exists_and_not_empty(file_name):
    return Path(file_name).is_file() and os.stat(file_name).st_size != 0