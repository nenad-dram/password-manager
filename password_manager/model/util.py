'''
Created on Feb 27, 2020

@author: ndramica
'''
from datetime import datetime
import pyperclip

def get_current_date():
    return datetime.today().strftime('%Y-%m-%d %H:%M:%S')

def copy_to_clipboard(text):
    pyperclip.copy(text)