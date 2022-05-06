"""
GUI module entry search form.

Generated by PAGE version 4.26
in conjunction with Tcl version 8.6

Created on Feb 29, 2020
@author: nenad.dramicanin
"""

import tkinter as tk

import support.entry_search_support as entry_search_support
import view.window_util as window_util


def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = SearchEntryWidnow(root)
    entry_search_support.init(root, top)
    root.mainloop()
    w = None


def create_search_entry_window(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_SearchEntryWidnow(root, *args, **kwargs)' .'''
    global w, w_win, root
    root = rt
    w = tk.Toplevel(root)
    top = SearchEntryWidnow(w)
    entry_search_support.init(w, top, *args, **kwargs)
    return w, top


def destroy_search_entry_window():
    global w
    w.destroy()
    w = None


class SearchEntryWidnow:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        
        width = 383
        height = 200
        
        center = window_util.get_center_points(top, width, height)
        
        top.geometry("{}x{}+{}+{}".format(width, height, center[0], center[1]))

        top.minsize(176, 1)
        top.maxsize(5764, 1590)
        top.resizable(0, 0)
        top.title("Search Entry")
        top.configure(highlightcolor="black")

        self.frameBody = tk.Frame(top)
        self.frameBody.place(relx=0.0, rely=0.0, relheight=1.0, relwidth=1.0)
        self.frameBody.configure(relief='groove')
        self.frameBody.configure(borderwidth="2")
        self.frameBody.configure(background="#d9d9d9")
        self.frameBody.configure(highlightbackground="#d9d9d9")
        self.frameBody.configure(highlightcolor="black")

        self.lblType = tk.Label(self.frameBody)
        self.lblType.place(relx=0.026, rely=0.135, height=19, width=67)
        self.lblType.configure(activebackground="#f9f9f9")
        self.lblType.configure(activeforeground="black")
        self.lblType.configure(anchor='w')
        self.lblType.configure(background="#d9d9d9")
        self.lblType.configure(disabledforeground="#a3a3a3")
        self.lblType.configure(foreground="#000000")
        self.lblType.configure(highlightbackground="#d9d9d9")
        self.lblType.configure(highlightcolor="black")
        self.lblType.configure(text='''Type:''')

        self.selType = tk.StringVar()
        self.selType.set("Please select")
        self.typeSelMenu = tk.OptionMenu(self.frameBody, self.selType, None)
        self.typeSelMenu.place(relx=0.235, rely=0.135, height=21, relwidth=0.715)
        self.typeSelMenu.configure(background="#d9d9d9")
        self.typeSelMenu.configure(highlightbackground="#d3d3d3")
        self.typeSelMenu.configure(foreground="#000000")
        self.typeSelMenu.configure(activebackground="#a7a7a7")
        self.typeSelMenu.configure(activeforeground="#000000")

        self.lblCateg = tk.Label(self.frameBody)
        self.lblCateg.place(relx=0.026, rely=0.31, height=15, width=67)
        self.lblCateg.configure(activebackground="#f9f9f9")
        self.lblCateg.configure(activeforeground="black")
        self.lblCateg.configure(anchor='w')
        self.lblCateg.configure(background="#d9d9d9")
        self.lblCateg.configure(disabledforeground="#a3a3a3")
        self.lblCateg.configure(foreground="#000000")
        self.lblCateg.configure(highlightbackground="#d9d9d9")
        self.lblCateg.configure(highlightcolor="black")
        self.lblCateg.configure(text='''Category:''')
        
        self.selCat = tk.StringVar()
        self.selCat.set("Please select")
        self.catSelMenu = tk.OptionMenu(self.frameBody, self.selCat, None)
        self.catSelMenu.place(relx=0.235, rely=0.31,height=21, relwidth=0.715)
        self.catSelMenu.configure(background="#d9d9d9")
        self.catSelMenu.configure(highlightbackground="#d3d3d3")
        self.catSelMenu.configure(foreground="#000000")
        self.catSelMenu.configure(activebackground="#a7a7a7")
        self.catSelMenu.configure(activeforeground="#000000")

        self.lblName = tk.Label(self.frameBody)
        self.lblName.place(relx=0.026, rely=0.5, height=15, width=67)
        self.lblName.configure(activebackground="#f9f9f9")
        self.lblName.configure(activeforeground="black")
        self.lblName.configure(anchor='w')
        self.lblName.configure(background="#d9d9d9")
        self.lblName.configure(disabledforeground="#a3a3a3")
        self.lblName.configure(foreground="#000000")
        self.lblName.configure(highlightbackground="#d9d9d9")
        self.lblName.configure(highlightcolor="black")
        self.lblName.configure(text='''Name:''')

        self.entryName = tk.Entry(self.frameBody)
        self.entryName.place(relx=0.235, rely=0.5, height=21, relwidth=0.715)
        self.entryName.configure(background="white")
        self.entryName.configure(disabledforeground="#a3a3a3")
        self.entryName.configure(font="TkFixedFont")
        self.entryName.configure(foreground="#000000")
        self.entryName.configure(highlightbackground="#d9d9d9")
        self.entryName.configure(highlightcolor="black")
        self.entryName.configure(insertbackground="black")
        self.entryName.configure(selectbackground="#c4c4c4")
        self.entryName.configure(selectforeground="black")

        self.btnSearch = tk.Button(self.frameBody)
        self.btnSearch.place(relx=0.757, rely=0.665, height=21, width=67)
        self.btnSearch.configure(activebackground="#ececec")
        self.btnSearch.configure(activeforeground="#000000")
        self.btnSearch.configure(background="#d9d9d9")
        self.btnSearch.configure(disabledforeground="#a3a3a3")
        self.btnSearch.configure(foreground="#000000")
        self.btnSearch.configure(highlightbackground="#d9d9d9")
        self.btnSearch.configure(highlightcolor="black")
        self.btnSearch.configure(pady="0")
        self.btnSearch.configure(text='''Search''')

        self.btnCancel = tk.Button(self.frameBody)
        self.btnCancel.place(relx=0.548, rely=0.665, height=21, width=67)
        self.btnCancel.configure(activebackground="#ececec")
        self.btnCancel.configure(activeforeground="#000000")
        self.btnCancel.configure(background="#d9d9d9")
        self.btnCancel.configure(disabledforeground="#a3a3a3")
        self.btnCancel.configure(foreground="#000000")
        self.btnCancel.configure(highlightbackground="#d9d9d9")
        self.btnCancel.configure(highlightcolor="black")
        self.btnCancel.configure(pady="0")
        self.btnCancel.configure(text='''Cancel''')

        self.lblMsg = tk.Label(self.frameBody)
        self.lblMsg.place(relx=0.026, rely=0.81, height=23, width=355)
        self.lblMsg.configure(activebackground="#f9f9f9")
        self.lblMsg.configure(background="#d9d9d9")
        self.lblMsg.configure(disabledforeground="#a3a3a3")
        self.lblMsg.configure(foreground="#ff0000")
