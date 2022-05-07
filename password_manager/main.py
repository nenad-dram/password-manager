"""
Entry point of the application

Created on Jan 20, 2020
@author: nenad.dramicanin
"""
import tkinter as tk

import model.security as security
import view.login as login
import view.registration as registration
import view.window_util as window_util
import sys

root = tk.Tk(className=window_util.get_app_name())

# Configure application wide exception handler
sys.excepthook = window_util.handle_app_exception

# Login or Registration window will be shown based on a master password existence
if security.master_pwd_exists():
    login.create_login_window(root)
else:
    registration.create_registration_window(root)

root.wm_iconphoto(root._w, tk.PhotoImage(file=window_util.get_icon_path()))
root.mainloop()
