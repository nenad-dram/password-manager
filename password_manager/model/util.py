'''
Created on Feb 27, 2020

@author: ndramica
'''
from datetime import datetime
import pyperclip
import pathlib
import os
import sys


def get_current_date():
    return datetime.today().strftime('%Y-%m-%d %H:%M:%S')


def copy_to_clipboard(text):
    pyperclip.copy(text)


def file_exists_and_not_empty(file_name):
    return pathlib.Path(file_name).is_file() and os.stat(file_name).st_size != 0


def get_root_path():
    return sys._MEIPASS if getattr(sys, 'frozen', False) else \
        os.path.join(os.path.dirname(__file__), os.pardir, os.pardir)