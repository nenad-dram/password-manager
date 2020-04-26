#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.26
#  in conjunction with Tcl version 8.6
#    Feb 03, 2020 09:01:07 AM CET  platform: Windows NT

import sys
import view.window_util as window_util
import tkinter as tk
import support.main_window_support as main_window_support
import platform
from tkinter import ttk

def create_main_window(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    top = MainWindow (root)
    main_window_support.init(root, top, *args, **kwargs)


def destroy_main_window():
    global w
    w.destroy()
    w = None


class MainWindow():
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.', background=_bgcolor)
        self.style.configure('.', foreground=_fgcolor)
        self.style.configure('.', font="TkDefaultFont")
        self.style.map('.', background=[('selected', _compcolor), ('active', _ana2color)])
        
        width = 700
        height = 527

        center = window_util.get_center_points(top, width, height)

        top.geometry("{}x{}+{}+{}".format(width, height, center[0], center[1]))

        top.minsize(176, 1)
        top.maxsize(rt.winfo_screenwidth(), rt.winfo_screenheight())
        top.resizable(0, 0)
        top.title("Password Manager")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        top.iconbitmap(window_util.get_icon_path())
        
        self.header = tk.Frame(top)
        self.header.place(relx=0.0, rely=0.0, relheight=0.106, relwidth=1.0)
        self.header.configure(relief='groove')
        self.header.configure(borderwidth="2")
        self.header.configure(relief="groove")
        self.header.configure(background="#d9d9d9")
        self.header.configure(highlightbackground="#d9d9d9")
        self.header.configure(highlightcolor="black")

        self.frameActBtn = ttk.Frame(self.header)
        self.frameActBtn.place(relx=0.81, rely=0.0, relheight=1.0, relwidth=0.3)
        self.frameActBtn.configure(relief='groove')
        self.frameActBtn.configure(borderwidth="2")
        self.frameActBtn.configure(relief="groove")

        self.btnInfo = tk.Button(self.frameActBtn)
        self.btnInfo.place(relx=0.14, rely=0.1, width=75, height=28)
        self.btnInfo.configure(activebackground="#ececec")
        self.btnInfo.configure(activeforeground="#000000")
        self.btnInfo.configure(background="#d9d9d9")
        self.btnInfo.configure(disabledforeground="#a3a3a3")
        self.btnInfo.configure(foreground="#000000")
        self.btnInfo.configure(highlightbackground="#d9d9d9")
        self.btnInfo.configure(highlightcolor="black")
        self.btnInfo.configure(pady="0")
        self.btnInfo.configure(text='''Details''')
        self.btnInfo.configure(state="disabled")

        self.frameMenuBtns = tk.Frame(self.header)
        self.frameMenuBtns.place(relx=0.0, rely=0.0, relheight=1.0, relwidth=0.26)
        self.frameMenuBtns.configure(relief='groove')
        self.frameMenuBtns.configure(borderwidth="2")
        self.frameMenuBtns.configure(relief="groove")
        self.frameMenuBtns.configure(background="#d9d9d9")

        self.btnNewEnt = tk.Button(self.frameMenuBtns)
        self.btnNewEnt.place(relx=0.05, rely=0.18, height=28, width=75)
        self.btnNewEnt.configure(activebackground="#ececec")
        self.btnNewEnt.configure(activeforeground="#000000")
        self.btnNewEnt.configure(background="#d9d9d9")
        self.btnNewEnt.configure(disabledforeground="#a3a3a3")
        self.btnNewEnt.configure(foreground="#000000")
        self.btnNewEnt.configure(highlightbackground="#d9d9d9")
        self.btnNewEnt.configure(highlightcolor="black")
        self.btnNewEnt.configure(pady="0")
        self.btnNewEnt.configure(text='''New Entry''')
        
        self.btnSearch = tk.Button(self.frameMenuBtns)
        self.btnSearch.place(relx=0.52, rely=0.18, height=28, width=75)
        self.btnSearch.configure(activebackground="#ececec")
        self.btnSearch.configure(activeforeground="#000000")
        self.btnSearch.configure(background="#d9d9d9")
        self.btnSearch.configure(disabledforeground="#a3a3a3")
        self.btnSearch.configure(foreground="#000000")
        self.btnSearch.configure(highlightbackground="#d9d9d9")
        self.btnSearch.configure(highlightcolor="black")
        self.btnSearch.configure(pady="0")
        self.btnSearch.configure(text='''Search''')

        self.Frame = tk.Frame(top)
        self.Frame.place(relx=0.0, rely=0.088, relheight=0.849, relwidth=1.0)
        self.Frame.configure(relief='groove')
        self.Frame.configure(borderwidth="2")
        self.Frame.configure(relief="groove")
        self.Frame.configure(background="#d9d9d9")
        self.Frame.configure(highlightbackground="#d9d9d9")
        self.Frame.configure(highlightcolor="black")

        self.style.configure('Treeview',  font="TkDefaultFont")
        self.treeviewRows = ScrolledTreeView(self.Frame)
        self.treeviewRows.place(relx=0.0, rely=0.0, relheight=1.0, relwidth=1.0)
        self.treeviewRows.configure(columns="name category type")
        # build_treeview_support starting.
        self.treeviewRows.heading("#0", text="ID")
        self.treeviewRows.heading("#0", anchor="center")
        self.treeviewRows.column("#0", width="0")
        self.treeviewRows.column("#0", minwidth="0")
        self.treeviewRows.column("#0", stretch="0")
        self.treeviewRows.column("#0", anchor="c")
        self.treeviewRows.heading("name", text="Name")
        self.treeviewRows.heading("name", anchor="center")
        self.treeviewRows.column("name", width="150")
        self.treeviewRows.column("name", minwidth="20")
        self.treeviewRows.column("name", stretch="1")
        self.treeviewRows.column("name", anchor="c")
        self.treeviewRows.heading("category", text="Category")
        self.treeviewRows.heading("category", anchor="center")
        self.treeviewRows.column("category", width="150")
        self.treeviewRows.column("category", minwidth="20")
        self.treeviewRows.column("category", stretch="1")
        self.treeviewRows.column("category", anchor="c")
        self.treeviewRows.heading("type", text="Type")
        self.treeviewRows.heading("type", anchor="center")
        self.treeviewRows.column("type", width="150")
        self.treeviewRows.column("type", minwidth="20")
        self.treeviewRows.column("type", stretch="1")
        self.treeviewRows.column("type", anchor="c")
        
        self.menubar = tk.Menu(top, font="TkMenuFont", bg=_bgcolor, fg=_fgcolor)
        top.configure(menu=self.menubar)

        self.sub_menu = tk.Menu(top, tearoff=0)
        self.menubar.add_cascade(
                menu=self.sub_menu,
                activebackground="#ececec",
                activeforeground="#000000",
                background="#d9d9d9",
                font="TkMenuFont",
                foreground="#000000",
                label="Menu")
        self.sub_menu.add_command(
                activebackground="#ececec",
                activeforeground="#000000",
                background="#d9d9d9",
                font="TkMenuFont",
                foreground="#000000",
                label="Categories")
        self.sub_menu.add_command(
                activebackground="#ececec",
                activeforeground="#000000",
                background="#d9d9d9",
                font="TkMenuFont",
                foreground="#000000",
                label="Set default e-mail")
        self.sub_menu.add_command(
                activebackground="#ececec",
                activeforeground="#000000",
                background="#d9d9d9",
                font="TkMenuFont",
                foreground="#000000",
                label="Change Master Password")
        self.sub_menu.add_command(
                activebackground="#ececec",
                activeforeground="#000000",
                background="#d9d9d9",
                font="TkMenuFont",
                foreground="#000000",
                label="Reset all")
        self.sub_menu.add_separator(
                background="#d9d9d9")
        self.sub_menu.add_command(
                activebackground="#ececec",
                activeforeground="#000000",
                background="#d9d9d9",
                font="TkMenuFont",
                foreground="#000000",
                label="Quit")


# The following code is added to facilitate the Scrolled widgets you specified.
class AutoScroll(object):
    '''Configure the scrollbars for a widget.'''

    def __init__(self, master):
        #  Rozen. Added the try-except clauses so that this class
        #  could be used for scrolled entry widget for which vertical
        #  scrolling is not supported. 5/7/14.
        try:
            vsb = ttk.Scrollbar(master, orient='vertical', command=self.yview)
        except:
            pass
        hsb = ttk.Scrollbar(master, orient='horizontal', command=self.xview)

        #self.configure(yscrollcommand=_autoscroll(vsb),
        #    xscrollcommand=_autoscroll(hsb))
        try:
            self.configure(yscrollcommand=self._autoscroll(vsb))
        except:
            pass
        self.configure(xscrollcommand=self._autoscroll(hsb))

        self.grid(column=0, row=0, sticky='nsew')
        try:
            vsb.grid(column=1, row=0, sticky='ns')
        except:
            pass
        hsb.grid(column=0, row=1, sticky='ew')

        master.grid_columnconfigure(0, weight=1)
        master.grid_rowconfigure(0, weight=1)

        # Copy geometry methods of master  (taken from ScrolledText.py)
        methods = tk.Pack.__dict__.keys() | tk.Grid.__dict__.keys() | tk.Place.__dict__.keys()

        for meth in methods:
            if meth[0] != '_' and meth not in ('config', 'configure'):
                setattr(self, meth, getattr(master, meth))

    @staticmethod
    def _autoscroll(sbar):
        '''Hide and show scrollbar as needed.'''
        def wrapped(first, last):
            first, last = float(first), float(last)
            if first <= 0 and last >= 1:
                sbar.grid_remove()
            else:
                sbar.grid()
            sbar.set(first, last)
        return wrapped

    def __str__(self):
        return str(self.master)


def _create_container(func):
    '''Creates a ttk Frame with a given master, and use this new frame to
    place the scrollbars and the widget.'''
    def wrapped(cls, master, **kw):
        container = ttk.Frame(master)
        container.bind('<Enter>', lambda e: _bound_to_mousewheel(e, container))
        container.bind('<Leave>', lambda e: _unbound_to_mousewheel(e, container))
        return func(cls, container, **kw)
    return wrapped


class ScrolledTreeView(AutoScroll, ttk.Treeview):
    '''A standard ttk Treeview widget with scrollbars that will
    automatically show/hide as needed.'''
    @_create_container
    def __init__(self, master, **kw):
        ttk.Treeview.__init__(self, master, **kw)
        AutoScroll.__init__(self, master)


def _bound_to_mousewheel(event, widget):
    child = widget.winfo_children()[0]
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        child.bind_all('<MouseWheel>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-MouseWheel>', lambda e: _on_shiftmouse(e, child))
    else:
        child.bind_all('<Button-4>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Button-5>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-Button-4>', lambda e: _on_shiftmouse(e, child))
        child.bind_all('<Shift-Button-5>', lambda e: _on_shiftmouse(e, child))


def _unbound_to_mousewheel(event, widget):
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        widget.unbind_all('<MouseWheel>')
        widget.unbind_all('<Shift-MouseWheel>')
    else:
        widget.unbind_all('<Button-4>')
        widget.unbind_all('<Button-5>')
        widget.unbind_all('<Shift-Button-4>')
        widget.unbind_all('<Shift-Button-5>')


def _on_mousewheel(event, widget):
    if platform.system() == 'Windows':
        widget.yview_scroll(-1*int(event.delta/120),'units')
    elif platform.system() == 'Darwin':
        widget.yview_scroll(-1*int(event.delta),'units')
    else:
        if event.num == 4:
            widget.yview_scroll(-1, 'units')
        elif event.num == 5:
            widget.yview_scroll(1, 'units')


def _on_shiftmouse(event, widget):
    if platform.system() == 'Windows':
        widget.xview_scroll(-1*int(event.delta/120), 'units')
    elif platform.system() == 'Darwin':
        widget.xview_scroll(-1*int(event.delta), 'units')
    else:
        if event.num == 4:
            widget.xview_scroll(-1, 'units')
        elif event.num == 5:
            widget.xview_scroll(1, 'units')

