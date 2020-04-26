#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.26
#  in conjunction with Tcl version 8.6
#    Jan 24, 2020 03:26:07 PM CET  platform: Windows NT

from support import login_support

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

from view import window_util

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    root.iconbitmap('../resources/padlock.ico')
    top = LoginWindow (root)
    login_support.init(root, top)
    root.mainloop()
    w = None

def create_loginWindow(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    top = LoginWindow (root)
    login_support.init(root, top, *args, **kwargs)

def destroy_loginWindow():
    global w
    w.destroy()
    w = None

class LoginWindow():
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        
        width = 397
        height = 176
        
        center = window_util.get_center_points(top, width, height)
        
        top.geometry("{}x{}+{}+{}".format(width, height, center[0], center[1]))
        top.minsize(176, 1)
        top.maxsize(5764, 1590)
        top.resizable(0, 0)
        top.title("Login")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.lblWelcomeTxt = tk.Label(top)
        self.lblWelcomeTxt.place(relx=0.0, rely=0.057, height=31, width=387)
        self.lblWelcomeTxt.configure(activebackground="#f9f9f9")
        self.lblWelcomeTxt.configure(activeforeground="black")
        self.lblWelcomeTxt.configure(background="#d9d9d9")
        self.lblWelcomeTxt.configure(disabledforeground="#a3a3a3")
        self.lblWelcomeTxt.configure(font="-family {Segoe UI} -size 12 -weight bold")
        self.lblWelcomeTxt.configure(foreground="#000000")
        self.lblWelcomeTxt.configure(highlightbackground="#d9d9d9")
        self.lblWelcomeTxt.configure(highlightcolor="black")
        self.lblWelcomeTxt.configure(text='''Welcome to Password Manager''')

        self.lblInsertPwd = tk.Label(top)
        self.lblInsertPwd.place(relx=0.025, rely=0.284, height=21, width=357)
        self.lblInsertPwd.configure(activebackground="#f9f9f9")
        self.lblInsertPwd.configure(activeforeground="black")
        self.lblInsertPwd.configure(background="#d9d9d9")
        self.lblInsertPwd.configure(disabledforeground="#a3a3a3")
        self.lblInsertPwd.configure(font="-family {Segoe UI} -size 10")
        self.lblInsertPwd.configure(foreground="#000000")
        self.lblInsertPwd.configure(highlightbackground="#d9d9d9")
        self.lblInsertPwd.configure(highlightcolor="black")
        self.lblInsertPwd.configure(text='''Please enter master password''')

        self.entMasterPwd = tk.Entry(top)
        self.entMasterPwd.place(relx=0.202, rely=0.511, height=23
                , relwidth=0.564)
        self.entMasterPwd.configure(background="white")
        self.entMasterPwd.configure(disabledforeground="#a3a3a3")
        self.entMasterPwd.configure(font="-family {Courier New} -size 9")
        self.entMasterPwd.configure(foreground="#000000")
        self.entMasterPwd.configure(highlightbackground="#d9d9d9")
        self.entMasterPwd.configure(highlightcolor="black")
        self.entMasterPwd.configure(insertbackground="black")
        self.entMasterPwd.configure(selectbackground="#c4c4c4")
        self.entMasterPwd.configure(selectforeground="black")
        self.entMasterPwd.configure(show="*")

        self.btnLogin = tk.Button(top)
        self.btnLogin.place(relx=0.353, rely=0.71, height=32, width=98)
        self.btnLogin.configure(activebackground="#ececec")
        self.btnLogin.configure(activeforeground="#000000")
        self.btnLogin.configure(background="#d9d9d9")
        self.btnLogin.configure(cursor="arrow")
        self.btnLogin.configure(disabledforeground="#a3a3a3")
        self.btnLogin.configure(font="-family {Segoe UI} -size 9 -weight bold")
        self.btnLogin.configure(foreground="#000000")
        self.btnLogin.configure(highlightbackground="#d9d9d9")
        self.btnLogin.configure(highlightcolor="black")
        self.btnLogin.configure(pady="0")
        self.btnLogin.configure(text='''Login''')
    


