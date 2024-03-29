"""
Support GUI module for showing entry details.

Generated by PAGE version 4.26
in conjunction with Tcl version 8.6

Created on Feb 16, 2020
@author: nenad.dramicanin
"""

import model.data_model as data_model
import model.services as services
import model.settings as settings
import model.util as util
import tkinter as tk


def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top
    gui.update_parent = False
    gui.btnClose.configure(command=destroy_window)

    # Configuring type option list
    type_menu = gui.typeSelMenu["menu"]
    type_menu.delete(0, "end")
    for val in [e.value for e in data_model.EntryType]:
        type_menu.add_command(label=val, command=lambda value=val: gui.selType.set(value))
        type_menu.configure(activebackground="#a7a7a7", background="#d9d9d9")
        type_menu.configure(foreground="#000000", activeforeground="#000000")

    # Configuring category option list
    cat_menu = gui.catSelMenu["menu"]
    cat_menu.delete(0, "end")
    for val in [c.name for c in services.category_list()]:
        cat_menu.add_command(label=val, command=lambda value=val: gui.selCat.set(value))
        cat_menu.configure(background="#d9d9d9", activebackground="#a7a7a7")
        cat_menu.configure(foreground="#000000", activeforeground="#000000")

    fill_form(args[0])

    gui.chBtnShow.configure(command=lambda: gui.entryValue.configure(show="" if w.setChBtnShow.get() else "*"))
    gui.btnEdit.configure(command=lambda: enable_for_edit(True))
    gui.btnSave.configure(command=lambda: on_save(args[0]))
    gui.btnDelete.configure(command=lambda: on_delete(args[0].entity_id))
    gui.selType.trace('w', on_option_select)
    
    conf_copy_btns(args[0])


def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None


def fill_form(entry: data_model.Entry):
    """Fills the form with Entry's data and disables all fields"""

    w.entryId.insert(0, entry.entity_id)
    w.selType.set(entry.entry_type)
    category = services.category_get_by_id(entry.category_id)
    w.selCat.set(category.name)
    w.entryName.insert(0, entry.name)
    w.entryValue.insert(0, entry.value)
    w.entryUsername.insert(0, entry.username)
    w.entryEmail.insert(0, entry.email)
    w.textDesc.insert('1.0', entry.description)
    w.entryModDate.insert(0, entry.modified_date)
    
    w.entryId.configure(state="readonly")
    w.entryModDate.configure(state="readonly")
    
    enable_for_edit(False)


def on_save(entry: data_model.Entry):
    """Validates form data and initiates save action"""

    sel_type = w.selType.get()
    sel_catg = w.selCat.get()
    name = w.entryName.get()
    value = w.entryValue.get()
    description = w.textDesc.get("1.0", tk.END) if not w.textDesc.get("1.0", tk.END).isspace() else ""
    
    email = w.entryEmail.get()
    username = w.entryUsername.get()   

    # Name is mandatory field
    if name.isspace() or len(name) == 0:
        w.lblMsg.configure(text='Name can\'t be empty!')
        return

    # Value is mandatory field
    if value.isspace() or len(value) == 0:
        w.lblMsg.configure(text='Value can\'t be empty!')
        return

    # For 'Account' entries either e-mail or username must be defined (or both)
    if (sel_type == data_model.EntryType.ACCOUNT.value and ((email.isspace() or len(email) == 0)
                                                            and (username.isspace() or len(username) == 0))):
        w.lblMsg.configure(text='Account must have username or e-mail value!')
        return
    
    entry.entry_type = sel_type
    entry.category_id = services.category_get_by_name(sel_catg).entity_id
    entry.name = name
    entry.value = value
    entry.email = email
    entry.username = username
    entry.description = description
    
    services.entry_edit(entry)
    
    w.lblMsg.configure(foreground="#008000")
    w.lblMsg.configure(text='Entry updated!')
    
    w.update_parent = True
    destroy_window()


def on_delete(entry_id: int):
    """Initiates delete action"""

    services.entry_delete(entry_id)
    w.lblMsg.configure(foreground="#008000")
    w.lblMsg.configure(text='Entry deleted!')
    w.update_parent = True
    destroy_window()    


def enable_for_edit(to_enable: bool):
    """Enables or disables fields and button based on to_enable parameter"""

    enable_state = "normal" if to_enable else "disabled"
    w.typeSelMenu.configure(state=enable_state)
    w.catSelMenu.configure(state=enable_state)
    w.entryName.configure(state=enable_state)
    w.entryValue.configure(state=enable_state)
    w.textDesc.configure(state=enable_state)
        
    w.btnSave.configure(state=enable_state)
    on_option_select()
    
    w.btnEdit.configure(state="normal" if not to_enable else "disabled")


def on_option_select(*args):
    """Based on an entry type handles e-mail and username field.

    If option 'Account' is selected then e-mail and username fields will be enabled and filled with existing values
    """

    option = w.selType.get()
    state_val = "disabled"
    if option == "account":
        state_val = "normal"
    else:
        w.entryEmail.delete(0, 'end')
        w.entryUsername.delete(0, 'end')
            
    w.entryEmail.configure(state=state_val)
    w.entryUsername.configure(state=state_val)

    # Enables 'Default e-mail' checkbox if one is defined
    if settings.get_default_email() is not None and settings.get_default_email() != "":
        w.checkDefEmail.configure(state=state_val)
        w.checkDefEmail.configure(command=on_check_email)


def on_check_email():
    """Sets e-mail field value to defined default e-mail"""

    email = ""
    if w.chDfEmVal.get():
        email = settings.get_default_email()
    w.entryEmail.delete(0, 'end')  
    w.entryEmail.insert(0, email)


def conf_copy_btns(entry: data_model.Entry):
    """Configures buttons used to copy one of the form parameters into clipboard.

    Value, e-mail or username can be copied. The latter two are available only if entry type is Account
    """

    w.btnCopyVal.configure(command=lambda: util.copy_to_clipboard(w.entryValue.get()))

    if entry.entry_type == "account" and len(entry.email) > 0:
        w.btnCopyEmail.configure(state="normal")
        w.btnCopyEmail.configure(command=lambda: util.copy_to_clipboard(entry.email))
    if entry.entry_type == "account" and len(entry.username) > 0:
        w.btnCopyUser.configure(state="normal")
        w.btnCopyUser.configure(command=lambda: util.copy_to_clipboard(entry.username))