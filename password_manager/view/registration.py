#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.26
#  in conjunction with Tcl version 8.6
#    Jan 23, 2020 05:51:23 PM CET  platform: Windows NT

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

from support import registration_support
from view import window_util


def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = RegistrationWindow (root)
    registration_support.init(root, top)
    root.mainloop()
    w = None
    
def create_registrationWindow(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    top = RegistrationWindow (root)
    registration_support.init(root, top, *args, **kwargs)

def destroy_registrationWindow():
    global w
    w.destroy()
    w = None

class RegistrationWindow:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        font10 = "-family {Segoe UI} -size 10 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"
        font11 = "-family {Segoe UI} -size 9 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"
        font12 = "-family {Courier New} -size 9 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"
        font13 = "-family {Segoe UI} -size 9 -weight bold -slant roman"  \
            " -underline 0 -overstrike 0"
        font9 = "-family {Segoe UI} -size 12 -weight bold -slant roman"  \
            " -underline 0 -overstrike 0"

        width = 445
        height = 280

        center = window_util.get_center_points(top, width, height)

        top.geometry("{}x{}+{}+{}".format(width, height, center[0], center[1]))
        
        top.minsize(176, 1)
        top.maxsize(5764, 1590)
        top.resizable(0, 0)
        top.title("Registration")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.lblWelcome = tk.Label(top)
        self.lblWelcome.place(relx=0.022, rely=0.038, height=41, width=427)
        self.lblWelcome.configure(activebackground="#f9f9f9")
        self.lblWelcome.configure(activeforeground="black")
        self.lblWelcome.configure(background="#d9d9d9")
        self.lblWelcome.configure(disabledforeground="#a3a3a3")
        self.lblWelcome.configure(font=font9)
        self.lblWelcome.configure(foreground="#000000")
        self.lblWelcome.configure(highlightbackground="#d9d9d9")
        self.lblWelcome.configure(highlightcolor="black")
        self.lblWelcome.configure(text='''Welcome to Password Manager''')

        self.lblMasterPwd = tk.Label(top)
        self.lblMasterPwd.place(relx=0.022, rely=0.23, height=31, width=417)
        self.lblMasterPwd.configure(activebackground="#f9f9f9")
        self.lblMasterPwd.configure(activeforeground="black")
        self.lblMasterPwd.configure(background="#d9d9d9")
        self.lblMasterPwd.configure(disabledforeground="#a3a3a3")
        self.lblMasterPwd.configure(font=font10)
        self.lblMasterPwd.configure(foreground="#000000")
        self.lblMasterPwd.configure(highlightbackground="#d9d9d9")
        self.lblMasterPwd.configure(highlightcolor="black")
        self.lblMasterPwd.configure(text='''Please enter new master password''')

        self.lblPwd = tk.Label(top)
        self.lblPwd.place(relx=0.023, rely=0.46, height=21, relwidth=0.35)
        self.lblPwd.configure(activebackground="#f9f9f9")
        self.lblPwd.configure(activeforeground="black")
        self.lblPwd.configure(anchor='w')
        self.lblPwd.configure(background="#d9d9d9")
        self.lblPwd.configure(disabledforeground="#a3a3a3")
        self.lblPwd.configure(font=font11)
        self.lblPwd.configure(foreground="#000000")
        self.lblPwd.configure(highlightbackground="#d9d9d9")
        self.lblPwd.configure(highlightcolor="black")
        self.lblPwd.configure(text='''Password:''')

        self.entPwd = tk.Entry(top)
        self.entPwd.place(relx=0.31, rely=0.46, height=20, relwidth=0.65)
        self.entPwd.configure(background="white")
        self.entPwd.configure(disabledforeground="#a3a3a3")
        self.entPwd.configure(font=font12)
        self.entPwd.configure(foreground="#000000")
        self.entPwd.configure(highlightbackground="#d9d9d9")
        self.entPwd.configure(highlightcolor="black")
        self.entPwd.configure(insertbackground="black")
        self.entPwd.configure(selectbackground="#c4c4c4")
        self.entPwd.configure(selectforeground="black")
        self.entPwd.configure(show="*")

        self.lblPwdCnf = tk.Label(top)
        self.lblPwdCnf.place(relx=0.023, rely=0.613, height=21, relwidth=0.35)
        self.lblPwdCnf.configure(activebackground="#f9f9f9")
        self.lblPwdCnf.configure(activeforeground="black")
        self.lblPwdCnf.configure(anchor='w')
        self.lblPwdCnf.configure(background="#d9d9d9")
        self.lblPwdCnf.configure(disabledforeground="#a3a3a3")
        self.lblPwdCnf.configure(font=font11)
        self.lblPwdCnf.configure(foreground="#000000")
        self.lblPwdCnf.configure(highlightbackground="#d9d9d9")
        self.lblPwdCnf.configure(highlightcolor="black")
        self.lblPwdCnf.configure(text='''Repeat password:''')

        self.entRptPwd = tk.Entry(top)
        self.entRptPwd.place(relx=0.31, rely=0.613, height=21, relwidth=0.65)
        self.entRptPwd.configure(background="white")
        self.entRptPwd.configure(disabledforeground="#a3a3a3")
        self.entRptPwd.configure(font=font12)
        self.entRptPwd.configure(foreground="#000000")
        self.entRptPwd.configure(highlightbackground="#d9d9d9")
        self.entRptPwd.configure(highlightcolor="black")
        self.entRptPwd.configure(insertbackground="black")
        self.entRptPwd.configure(selectbackground="#c4c4c4")
        self.entRptPwd.configure(selectforeground="black")
        self.entRptPwd.configure(show="*")

        self.btnSubmit = tk.Button(top)
        self.btnSubmit.place(relx=0.4, rely=0.766, height=32, width=98)
        self.btnSubmit.configure(activebackground="#ececec")
        self.btnSubmit.configure(activeforeground="#000000")
        self.btnSubmit.configure(background="#d9d9d9")
        self.btnSubmit.configure(disabledforeground="#a3a3a3")
        self.btnSubmit.configure(font=font13)
        self.btnSubmit.configure(foreground="#000000")
        self.btnSubmit.configure(highlightbackground="#d9d9d9")
        self.btnSubmit.configure(highlightcolor="black")
        self.btnSubmit.configure(pady="0")
        self.btnSubmit.configure(text='''Submit''')

        self.lblMsg = tk.Label(top)
        self.lblMsg.place(relx=0.0, rely=0.9, height=21, width=width)
        self.lblMsg.configure(background="#d9d9d9")
        self.lblMsg.configure(disabledforeground="#a3a3a3")
        self.lblMsg.configure(foreground="#ff0000")



