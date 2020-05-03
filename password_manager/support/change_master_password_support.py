"""
Support GUI module for changing master password.

Generated by PAGE version 4.26
in conjunction with Tcl version 8.6

Created on Feb 27, 2020
@author: nenad.dramicanin
"""

import model.security as security


def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top
    
    gui.btnCancel.configure(command = destroy_window)
    gui.btnChange.configure(command = on_change_btn)


def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None


def on_change_btn():
    """Validates form data and initiates change"""

    curr_pwd = w.entCurPwd.get().strip()
    new_pwd = w.entNewPwd.get().strip()
    rpt_pwd = w.entRptPwd.get().strip()
    
    if len(curr_pwd) == 0 or len(new_pwd) == 0 or len(rpt_pwd) == 0:
        w.lblMsg.configure(text="Please enter all values!")
        return
    
    if not security.master_pwd_valid(curr_pwd):
        w.lblMsg.configure(text="Invalid current password!")
        return
    
    if new_pwd != rpt_pwd:
        w.lblMsg.configure(text="New and Repeat password aren't equal!")
        return
    
    security.save_master_pwd(new_pwd)
    w.lblMsg.configure(foreground="#008000")
    w.lblMsg.configure(text="Password successfully changed!")