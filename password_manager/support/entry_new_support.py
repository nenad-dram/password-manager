#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 4.26
#  in conjunction with Tcl version 8.6
#    Feb 06, 2020 11:22:33 AM CET  platform: Windows NT

import sys
from model.data_model import EntryType
from model import services, settings

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
    gui.update_parent = False
    gui.btnCancel.configure(command = destroy_window)
    gui.btnCreate.configure(command = on_btn_create)
    type_menu=gui.typeSelMenu["menu"]
    type_menu.delete(0, "end")
    for val in [e.value for e in EntryType]:
            type_menu.add_command(label=val, command= lambda value=val: gui.selType.set(value))
    gui.selType.trace('w', on_option_select)
    
    cat_menu=gui.catSelMenu["menu"]
    cat_menu.delete(0, "end")
    for val in [c.name for c in services.category_list()]:
            cat_menu.add_command(label=val, command= lambda value=val: gui.selCat.set(value))

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

def on_option_select(*args):
    option = w.selType.get()
    stateVal = "disabled"
    if(option == "account"):
        stateVal = "normal"
    else:
        w.entryEmail.delete(0, 'end')
        w.entryUsername.delete(0, 'end')
        
    w.entryEmail.configure(state=stateVal)
    w.entryUsername.configure(state=stateVal)
    
    if settings.get_default_email() is not None and settings.get_default_email() != "":
        w.checkDefEmail.configure(state=stateVal)
        w.checkDefEmail.configure(command = on_check_email)

def on_btn_create():
    sel_type = w.selType.get()
    sel_catg = w.selCat.get()
    name = w.entryName.get()
    value = w.entryValue.get()
    description = w.textDesc.get("1.0", tk.END) if not w.textDesc.get("1.0", tk.END).isspace() else ""
    
    email = w.entryEmail.get()
    username = w.entryUsername.get()   
    
    if (sel_type == 'Please select'):
        w.lblMsg.config(text = 'Type can\'t be empty')
        return
    
    if (sel_catg == 'Please select'):
        w.lblMsg.config(text = 'Category can\'t be empty')
        return
    
    if (name.isspace() or len(name) == 0):
        w.lblMsg.config(text = 'Name can\'t be empty!')
        return
    
    if (value.isspace() or len(value) == 0):
        w.lblMsg.config(text = 'Value can\'t be empty!')
        return
    
    if (sel_type == 'account' and ((email.isspace() or len(email) == 0) 
                                   and (username.isspace() or len(username) == 0))):
        w.lblMsg.config(text = 'Account must have username or e-mail value!')
        return
      
    services.entry_add(name, value, sel_type, sel_catg, description, username, email)
    
    w.lblMsg.configure(foreground="#008000")
    w.lblMsg.config(text = 'New entry added!')
    w.update_parent = True
    destroy_window()

def on_check_email():
    email = ""
    if (w.chDfEmVal.get()):
        email = settings.get_default_email()
    w.entryEmail.delete(0, 'end')  
    w.entryEmail.insert(0, email)
    