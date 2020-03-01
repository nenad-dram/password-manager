#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.26
#  in conjunction with Tcl version 8.6
#    Feb 04, 2020 10:07:47 AM CET  platform: Windows NT

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

from support import category_new_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = CategoryNewWindow (root)
    category_new_support.init(root, top)
    root.mainloop()

w = None
def create_CategoryNewWindow(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    top = CategoryNewWindow (w)
    category_new_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_CategoryNewWindow():
    global w
    w.destroy()
    w = None

class CategoryNewWindow:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        
        width = 355
        height = 357
        
        center = get_center_points(width, height)
        
        top.geometry("{}x{}+{}+{}".format(width, height, center[0], center[1]))

        top.minsize(120, 1)
        top.maxsize(3844, 1061)
        top.resizable(1, 1)
        top.title("New Category")
        top.configure(background="#d9d9d9")
        top.grab_set()

        self.frameBody = tk.Frame(top)
        self.frameBody.place(relx=0.0, rely=0.0, relheight=1.0, relwidth=1.0)
        self.frameBody.configure(relief='groove')
        self.frameBody.configure(borderwidth="2")
        self.frameBody.configure(relief="groove")
        self.frameBody.configure(background="#d9d9d9")

        self.entName = tk.Entry(self.frameBody)
        self.entName.place(relx=0.31, rely=0.084, height=20, relwidth=0.577)
        self.entName.configure(background="white")
        self.entName.configure(disabledforeground="#a3a3a3")
        self.entName.configure(font="TkFixedFont")
        self.entName.configure(foreground="#000000")
        self.entName.configure(insertbackground="black")
 
        self.lblName = tk.Label(self.frameBody)
        self.lblName.place(relx=0.085, rely=0.084, height=21, width=54)
        self.lblName.configure(background="#d9d9d9")
        self.lblName.configure(disabledforeground="#a3a3a3")
        self.lblName.configure(foreground="#000000")
        self.lblName.configure(text='''Name:''')

        self.lblDescription = tk.Label(self.frameBody)
        self.lblDescription.place(relx=0.085, rely=0.223, height=21, width=76)
        self.lblDescription.configure(background="#d9d9d9")
        self.lblDescription.configure(disabledforeground="#a3a3a3")
        self.lblDescription.configure(foreground="#000000")
        self.lblDescription.configure(text='''Description:''')

        self.txtDescripton = tk.Text(self.frameBody)
        self.txtDescripton.place(relx=0.31, rely=0.223, relheight=0.514
                , relwidth=0.577)
        self.txtDescripton.configure(background="white")
        self.txtDescripton.configure(font="TkFixedFont")
        self.txtDescripton.configure(foreground="black")
        self.txtDescripton.configure(highlightbackground="#d9d9d9")
        self.txtDescripton.configure(highlightcolor="black")
        self.txtDescripton.configure(insertbackground="black")
        self.txtDescripton.configure(selectbackground="#c4c4c4")
        self.txtDescripton.configure(selectforeground="black")
        self.txtDescripton.configure(wrap="word")

        self.btnCreate = tk.Button(self.frameBody)
        self.btnCreate.place(relx=0.676, rely=0.782, height=24, width=77)
        self.btnCreate.configure(activebackground="#ececec")
        self.btnCreate.configure(activeforeground="#000000")
        self.btnCreate.configure(background="#d9d9d9")
        self.btnCreate.configure(disabledforeground="#a3a3a3")
        self.btnCreate.configure(foreground="#000000")
        self.btnCreate.configure(highlightbackground="#d9d9d9")
        self.btnCreate.configure(highlightcolor="black")
        self.btnCreate.configure(pady="0")
        self.btnCreate.configure(text='''Create''')

        self.btnCancel = tk.Button(self.frameBody)
        self.btnCancel.place(relx=0.423, rely=0.782, height=24, width=77)
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
        self.lblMsg.place(relx=0.028, rely=0.894, height=28, width=336)
        self.lblMsg.configure(background="#d9d9d9")
        self.lblMsg.configure(disabledforeground="#a3a3a3")
        self.lblMsg.configure(foreground="#ff0000")    
        
        set_icon()
        
def get_center_points(width, height):
    center_x = int((rt.winfo_screenwidth()/2) - (width/2))
    center_y = int((rt.winfo_screenheight()/2) - (height/2))
    return (center_x, center_y)

def set_icon():
    try:
        if (platform.system() == 'Linux'):
            root.iconbitmap('@../resources/padlock.xbm')
        else:
            root.iconbitmap('../resources/padlock.ico')
    except:
        print("Unable to load logo image")

