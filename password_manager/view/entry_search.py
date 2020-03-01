#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 5.0.1
#  in conjunction with Tcl version 8.6
#    Feb 29, 2020 02:16:38 PM CET  platform: Linux

import sys
from tkinter import StringVar, OptionMenu
import platform

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

from support import entry_search_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = SearchEntryWidnow (root)
    entry_search_support.init(root, top)
    root.mainloop()

w = None
def create_SearchEntryWidnow(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_SearchEntryWidnow(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    top = SearchEntryWidnow (w)
    entry_search_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_SearchEntryWidnow():
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
        
        center = get_center_points(width, height)
        
        top.geometry("{}x{}+{}+{}".format(width, height, center[0], center[1]))

        top.minsize(176, 1)
        top.maxsize(5764, 1590)
        top.resizable(1, 1)
        top.title("Search Entry")
        top.configure(highlightcolor="black")

        self.frameBody = tk.Frame(top)
        self.frameBody.place(relx=0.0, rely=0.0, relheight=1.0, relwidth=1.0)
        self.frameBody.configure(relief='groove')
        self.frameBody.configure(borderwidth="2")
        self.frameBody.configure(relief="groove")

        self.lblType = tk.Label(self.frameBody)
        self.lblType.place(relx=0.026, rely=0.135, height=19, width=67)
        self.lblType.configure(activebackground="#f9f9f9")
        self.lblType.configure(anchor='w')
        self.lblType.configure(text='''Type:''')

        
        self.selType=StringVar()
        self.selType.set("Please select")
        self.typeSelMenu = OptionMenu(self.frameBody, self.selType, None)
        self.typeSelMenu.place(relx=0.235, rely=0.135,height=21, relwidth=0.715)
        self.typeSelMenu.configure(background="#d9d9d9")
        self.typeSelMenu.configure(highlightbackground="#d9d9d9")
        self.typeSelMenu.configure(highlightcolor="black") 

        self.lblCateg = tk.Label(self.frameBody)
        self.lblCateg.place(relx=0.026, rely=0.31, height=15, width=67)
        self.lblCateg.configure(activebackground="#f9f9f9")
        self.lblCateg.configure(anchor='w')
        self.lblCateg.configure(text='''Category:''')
        
        self.selCat=StringVar()
        self.selCat.set("Please select")
        self.catSelMenu = OptionMenu(self.frameBody, self.selCat, None)
        self.catSelMenu.place(relx=0.235, rely=0.31,height=21, relwidth=0.715)
        self.catSelMenu.configure(background="#d9d9d9")
        self.catSelMenu.configure(highlightbackground="#d9d9d9")
        self.catSelMenu.configure(highlightcolor="black") 

        self.lblName = tk.Label(self.frameBody)
        self.lblName.place(relx=0.026, rely=0.5, height=15, width=67)
        self.lblName.configure(activebackground="#f9f9f9")
        self.lblName.configure(anchor='w')
        self.lblName.configure(text='''Name:''')

        self.entryName = tk.Entry(self.frameBody)
        self.entryName.place(relx=0.235, rely=0.5,height=21, relwidth=0.715)
        self.entryName.configure(background="white")
        self.entryName.configure(font="TkFixedFont")
        self.entryName.configure(selectbackground="#c4c4c4")

        self.btnSearch = tk.Button(self.frameBody)
        self.btnSearch.place(relx=0.757, rely=0.665, height=21, width=67)
        self.btnSearch.configure(activebackground="#f9f9f9")
        self.btnSearch.configure(pady="0")
        self.btnSearch.configure(text='''Search''')

        self.btnCancel = tk.Button(self.frameBody)
        self.btnCancel.place(relx=0.548, rely=0.665, height=21, width=67)
        self.btnCancel.configure(activebackground="#f9f9f9")
        self.btnCancel.configure(pady="0")
        self.btnCancel.configure(text='''Cancel''')

        self.lblMsg = tk.Label(self.frameBody)
        self.lblMsg.place(relx=0.026, rely=0.81, height=23, width=355)
        self.lblMsg.configure(activebackground="#f9f9f9")
        self.lblMsg.configure(background="#d9d9d9")
        self.lblMsg.configure(disabledforeground="#a3a3a3")
        self.lblMsg.configure(foreground="#ff0000")
        
        set_icon()

if __name__ == '__main__':
    vp_start_gui()

def get_center_points(width, height):
    center_x = int((root.winfo_screenwidth()/2) - (width/2))
    center_y = int((root.winfo_screenheight()/2) - (height/2))
    return (center_x, center_y)

def set_icon():
    try:
        if (platform.system() == 'Linux'):
            root.iconbitmap('@../resources/padlock.xbm')
        else:
            root.iconbitmap('../resources/padlock.ico')
    except:
        print("Unable to load logo image")
