#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 4.26
#  in conjunction with Tcl version 8.6
#    Feb 04, 2020 10:07:53 AM CET  platform: Windows NT

from model import services

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
    gui.btnCreate.configure(command = on_create_btn)
    gui.btnCancel.configure(command = destroy_window)


def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None


def on_create_btn():
    name = w.entName.get()
    description = w.txtDescripton.get("1.0", tk.END) if not w.txtDescripton.get("1.0", tk.END).isspace() else ""
    if name.isspace() or len(name) == 0:
        w.lblMsg.configure(text='Name can\'t be empty!')
        return
    services.category_add(name, description)
    destroy_window()