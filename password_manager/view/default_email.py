#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.26
#  in conjunction with Tcl version 8.6
#    Feb 26, 2020 12:39:14 PM CET  platform: Windows NT

import tkinter as tk
import support.default_email_support as default_email_support
import view.window_util as window_util


def create_default_email_window(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel(root)
    top = DefaultEmail(w)
    default_email_support.init(w, top, *args, **kwargs)
    return w, top


def destroy_default_email():
    global w
    w.destroy()
    w = None


class DefaultEmail:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        
        width = 450
        height = 112
        
        center = window_util.get_center_points(top, width, height)
        
        top.geometry("{}x{}+{}+{}".format(width, height, center[0], center[1]))
        
        top.minsize(120, 1)
        top.maxsize(3844, 1061)
        top.resizable(1, 1)
        top.title("Default E-mail")
        top.configure(background="#d9d9d9")

        top.iconbitmap(window_util.get_icon_path())

        self.entryEmail = tk.Entry(top)
        self.entryEmail.place(relx=0.253, rely=0.179, height=21, relwidth=0.694)
        self.entryEmail.configure(background="white")
        self.entryEmail.configure(disabledforeground="#a3a3a3")
        self.entryEmail.configure(font="TkFixedFont")
        self.entryEmail.configure(foreground="#000000")
        self.entryEmail.configure(insertbackground="black")

        self.lblEmail = tk.Label(top)
        self.lblEmail.place(relx=0.025, rely=0.179, height=21, width=100)
        self.lblEmail.configure(background="#d9d9d9")
        self.lblEmail.configure(disabledforeground="#a3a3a3")
        self.lblEmail.configure(foreground="#000000")
        self.lblEmail.configure(text='''Default e-mail:''')

        self.btnSave = tk.Button(top)
        self.btnSave.place(relx=0.785, rely=0.446, height=24, width=67)
        self.btnSave.configure(activebackground="#ececec")
        self.btnSave.configure(activeforeground="#000000")
        self.btnSave.configure(background="#d9d9d9")
        self.btnSave.configure(disabledforeground="#a3a3a3")
        self.btnSave.configure(foreground="#000000")
        self.btnSave.configure(highlightbackground="#d9d9d9")
        self.btnSave.configure(highlightcolor="black")
        self.btnSave.configure(pady="0")
        self.btnSave.configure(text='''Save''')

        self.btnCancel = tk.Button(top)
        self.btnCancel.place(relx=0.582, rely=0.446, height=24, width=67)
        self.btnCancel.configure(activebackground="#ececec")
        self.btnCancel.configure(activeforeground="#000000")
        self.btnCancel.configure(background="#d9d9d9")
        self.btnCancel.configure(disabledforeground="#a3a3a3")
        self.btnCancel.configure(foreground="#000000")
        self.btnCancel.configure(highlightbackground="#d9d9d9")
        self.btnCancel.configure(highlightcolor="black")
        self.btnCancel.configure(pady="0")
        self.btnCancel.configure(text='''Cancel''')

        self.lblMsg = tk.Label(top)
        self.lblMsg.place(relx=0.025, rely=0.714, height=21, width=374)
        self.lblMsg.configure(background="#d9d9d9")
        self.lblMsg.configure(disabledforeground="#a3a3a3")
        self.lblMsg.configure(foreground="#ff0000")
    




