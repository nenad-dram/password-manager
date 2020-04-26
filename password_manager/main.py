'''
Created on Jan 20, 2020

@author: nenad
'''

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

from model.security import master_pwd_exists
from view.login import create_loginWindow
from view.registration import create_registrationWindow
from view import window_util
import sys

root = tk.Tk()
sys.excepthook = window_util.handle_app_exception

if master_pwd_exists():
    create_loginWindow(root)
else:
    create_registrationWindow(root)

root.iconbitmap(window_util.get_icon_path())
root.mainloop()
