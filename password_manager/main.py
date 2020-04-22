'''
Created on Jan 20, 2020

@author: nenad
'''
import os
import platform

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

from model.security import master_pwd_exists
from view.login import create_loginWindow as start_login
from view.registration import create_registrationWindow as start_registration

root = tk.Tk()

if master_pwd_exists():
    start_login(root)
else:
    start_registration(root)
try:
    if platform.system() == 'Linux':
        root.iconbitmap('@'+os.path.join(os.path.dirname(__file__), '../resources/padlock.xbm'))
    else:
        root.iconbitmap(os.path.join(os.path.dirname(__file__), '../resources/padlock.ico'))
except:
    print("Unable to load logo image")

root.mainloop()
