#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 5.0.1
#  in conjunction with Tcl version 8.6
#    Feb 29, 2020 02:15:11 PM CET  platform: Linux

import sys
from model.data_model import EntryType
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
    
    root.update_parent = False
    w.btnCancel.configure(command = destroy_window)
    w.btnSearch.configure(command = on_search_btn)
    
    type_menu=gui.typeSelMenu["menu"]
    type_menu.delete(0, "end")
    for val in [e.value for e in EntryType]:
        type_menu.add_command(label=val, command= lambda value=val: gui.selType.set(value))
        type_menu.configure(activebackground="#a7a7a7", background="#d9d9d9")
        type_menu.configure(foreground="#000000", activeforeground="#000000")

    cat_menu=gui.catSelMenu["menu"]
    cat_menu.delete(0, "end")
    for val in [c.name for c in services.category_list()]:
        cat_menu.add_command(label=val, command= lambda value=val: gui.selCat.set(value))
        cat_menu.configure(background="#d9d9d9", activebackground="#a7a7a7")
        cat_menu.configure(foreground="#000000", activeforeground="#000000")

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

def on_search_btn():
    search_type = w.selType.get() if w.selType.get() != "Please select" else None
    search_ctg = w.selCat.get() if w.selCat.get() != "Please select" else None
    search_name = w.entryName.get()
        
    result = services.entity_search(search_ctg, search_type, search_name)
    
    if (len(result) == 0):
        w.lblMsg.configure(text="No entries found!")
    else:
        root.search_result = result
        root.update_parent = True
        destroy_window()
    