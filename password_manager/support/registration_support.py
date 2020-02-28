#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 4.26
#  in conjunction with Tcl version 8.6
#    Jan 23, 2020 05:53:07 PM CET  platform: Windows NT

import sys
from tkinter import messagebox
from model import security, settings
from view.login import vp_start_gui as start_login, create_loginWindow

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top
    gui.btnSubmit.configure(command = on_register_btn)

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None


def on_register_btn():
    global top_level
    password = w.entPwd.get().replace(' ', '')
    confirm_password = w.entRptPwd.get().replace(' ', '')
    if len(password) == 0 or len(confirm_password) == 0:
        messagebox.showerror('Registration', 'Please enter both values')
        return
    if password != confirm_password:
        messagebox.showerror('Registration', 'Password and Confirm password are different' )
        return
    settings.init()
    security.save_master_pwd(password)
    messagebox.showinfo('Registration', 'Registration successful, please login')
    
    destroy_window()
    create_loginWindow(tk.Tk())
    
