"""
Support GUI module for category management form.

Generated by PAGE version 4.26
in conjunction with Tcl version 8.6

Created on Feb 03, 2020
@author: nenad.dramicanin
"""
from tkinter import messagebox

import view.category_new as category_new
import view.category_details as category_details
import model.services as services


def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top
    gui.btnNewCat.configure(command=on_btn_create_new)
    gui.CategoryTreeView.bind('<<TreeviewSelect>>', on_row_select)
    insert_rows()


def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None


def on_btn_create_new():
    """Displays windows for creating new category"""

    child = category_new.create_category_new_window(root)
    root.wait_window(child[0])
    update_rows()


def insert_rows():
    """Shows existing categories on the form"""

    categories = services.category_list()
    for cat in categories:
        w.CategoryTreeView.insert('', 'end', text=cat.entity_id, values=(cat.name, cat.description))


def update_rows():
    """Updates form's category list and disables buttons on the form"""

    w.btnCatInfo.configure(state="disabled")
    w.btnCatEdit.configure(state="disabled")
    w.btnCatDelete.configure(state="disabled")
    w.CategoryTreeView.delete(*w.CategoryTreeView.get_children())
    insert_rows()


def on_row_select(event):
    """ Enables action buttons when a row is selected"""

    row_id = w.CategoryTreeView.item(event.widget.selection())["text"]
    w.btnCatInfo.configure(command=lambda: on_btn_cat_info(row_id))
    w.btnCatEdit.configure(command=lambda: on_btn_cat_edit(row_id))
    w.btnCatDelete.configure(command=lambda: on_btn_cat_delete(row_id))
    w.btnCatInfo.configure(state="normal")
    w.btnCatEdit.configure(state="normal")
    w.btnCatDelete.configure(state="normal")


def on_btn_cat_info(row_id: int):
    """Shows category details window"""

    category_details.create_category_details_window(root, 'info', services.category_get_by_id(row_id))


def on_btn_cat_edit(row_id: int):
    """Shows category edit window"""

    child = category_details.create_category_details_window(root, 'edit', services.category_get_by_id(row_id))
    root.wait_window(child[0])
    update_rows()


def on_btn_cat_delete(row_id: int):
    """Initiates category delete action"""

    if services.is_category_used(row_id):
        root.grab_set()
        messagebox.showerror("Delete category", "Category is in use!")
        return

    services.category_delete(row_id)
    messagebox.showinfo("Delete category", "Category deleted!")
    update_rows()
