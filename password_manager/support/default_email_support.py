"""
Support GUI module for changing default e-mail form.

Generated by PAGE version 4.26
in conjunction with Tcl version 8.6

Created on Feb 26, 2020
@author: nenad.dramicanin
"""

import model.settings as settings


def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top
    w.btnCancel.configure(command=destroy_window)
    w.btnSave.configure(command=save_email)
    w.entryEmail.insert(0, settings.get_default_email())


def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None


def save_email():
    email = w.entryEmail.get().replace(' ', '')
    settings.set_default_email(email)
    
    w.lblMsg.configure(text="E-mail saved!")
    w.lblMsg.configure(foreground="#008000")
