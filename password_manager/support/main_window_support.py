"""
Support GUI module for the main application window.

Generated by PAGE version 4.26
in conjunction with Tcl version 8.6

Created on Feb 03, 2020
@author: nenad.dramicanin
"""

from typing import List
import view.category_management as category_management
import view.default_email as default_email
import view.change_master_password as change_master_password
import view.entry_new as entry_new
import model.services as services
import model.security as security
import view.entry_details as entry_details
import view.entry_search as entry_search
import view.window_util as window_util
from tkinter import messagebox

# App data
from model import data_model

def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top

    # Configures top menu options
    gui.sub_menu.entryconfig(0, command=lambda: category_management.create_categ_man_window(top))
    gui.sub_menu.entryconfig(1, command=lambda: default_email.create_default_email_window(top))
    gui.sub_menu.entryconfig(2, command=lambda: change_master_password.create_change_master_pwd_window(top))
    gui.sub_menu.entryconfig(3, command=on_reset_req)
    gui.sub_menu.entryconfig(5, command=about_window)
    gui.sub_menu.entryconfig(6, command=destroy_window)

    gui.btnNewEnt.configure(command=on_create_new)
    gui.btnSearch.configure(command=on_search_btn)
    gui.treeviewRows.bind('<<TreeviewSelect>>', on_row_select)

    insert_rows(services.entry_list())


def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None


def insert_rows(entry_list: List[data_model.Entry]):
    """Inserts entries as tree view elements"""

    for ent in entry_list:
        category = services.category_get_by_id(ent.category_id).name
        w.treeviewRows.insert('', 'end', text=ent.entity_id, values=(ent.name, category, ent.entry_type))


def update_rows(entry_list: List[data_model.Entry]):
    """Inserts entries in the tree view, clears element selection and disables 'Info' button"""

    w.btnInfo.configure(state="disabled")
    w.treeviewRows.delete(*w.treeviewRows.get_children())
    insert_rows(entry_list)


def on_row_select(event):
    """Enables 'Info' button if an element is selected"""

    row_id = w.treeviewRows.item(event.widget.selection())["text"]
    w.btnInfo.configure(command=lambda: on_btn_info(row_id))
    w.btnInfo.configure(state="normal")


def on_btn_info(row_id):
    """Opens entry details window and waits for response so it can initialise list update"""

    child = entry_details.create_entry_details_window(root, services.entry_get_by_id(row_id))
    root.wait_window(child[0])
    if child[1].update_parent:
        update_rows(services.entry_list())


def on_create_new():
    """Opens entry new window and waits for response so it can initialise list update"""

    child = entry_new.create_new_entry_window(root)
    root.wait_window(child[0])
    if child[1].update_parent:
        update_rows(services.entry_list())


def on_reset_req():
    """Starts reset process after user confirmation """
    to_reset = messagebox.askyesno("Reset data", "All data will be removed. Are you sure?")
    if to_reset:
        security.reset_all()
        messagebox.showinfo("Reset data", "Data removed, please restart application")
        destroy_window()


def on_search_btn():
    """Opens entry search window and waits for response so it can initialise list update"""

    child = entry_search.create_search_entry_window(root)
    root.wait_window(child[0])
    if child[0].update_parent:
        update_rows(child[0].search_result)


def about_window():
    """Shows info with app details"""

    about_msg = window_util.get_app_name() +" " + window_util.get_app_version()
    messagebox.showinfo("About Application", about_msg)
