'''
Created on Jan 20, 2020

@author: nenad
'''
import platform

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

from model.security import master_pwd_exists
from view.login import create_loginWindow as start_login
from view.registration import create_registrationWindow as start_registration
 
root = tk.Tk()
 
if(master_pwd_exists()):
    start_login(root)
else:
    start_registration(root)
    
if (platform.system() == 'Linux'):
    root.iconbitmap('@../resources/padlock.xbm')
else:
    root.iconbitmap('../resources/padlock.ico')
root.mainloop()
