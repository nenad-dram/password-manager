#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.26
#  in conjunction with Tcl version 8.6
#    Feb 06, 2020 11:22:03 AM CET  platform: Windows NT

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

from support import entry_new_support
import os

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = NewEntryWindow (root)
    entry_new_support.init(root, top)
    root.mainloop()

w = None
def create_NewEntryWindow(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    top = NewEntryWindow (w)
    entry_new_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_NewEntryWidnow():
    global w
    w.destroy()
    w = None

class NewEntryWindow:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        
        width = 442
        height = 513

        center = get_center_points(width, height)

        top.geometry("{}x{}+{}+{}".format(width, height, center[0], center[1]))
        
        top.minsize(176, 1)
        top.maxsize(5764, 1590)
        top.resizable(1, 1)
        top.title("New Entry")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")
        
        top.grab_set()

        self.frameBody = tk.Frame(top)
        self.frameBody.place(relx=0.0, rely=0.0, relheight=1.05, relwidth=1.041)
        self.frameBody.configure(relief='groove')
        self.frameBody.configure(borderwidth="2")
        self.frameBody.configure(relief="groove")
        self.frameBody.configure(background="#d9d9d9")
        self.frameBody.configure(highlightbackground="#d9d9d9")
        self.frameBody.configure(highlightcolor="black")

        self.lblType = tk.Label(self.frameBody)
        self.lblType.place(relx=0.05, rely=0.055, height=21, width=92)
        self.lblType.configure(activebackground="#f9f9f9")
        self.lblType.configure(activeforeground="black")
        self.lblType.configure(anchor='w')
        self.lblType.configure(background="#d9d9d9")
        self.lblType.configure(disabledforeground="#a3a3a3")
        self.lblType.configure(foreground="#000000")
        self.lblType.configure(highlightbackground="#d9d9d9")
        self.lblType.configure(highlightcolor="black")
        self.lblType.configure(text='''Type:''')
        
        self.selType=StringVar()
        self.selType.set("Please select")
        self.typeSelMenu = OptionMenu(self.frameBody, self.selType, None)
        self.typeSelMenu.place(relx=0.3, rely=0.055, height=21, relwidth=0.596)
        self.typeSelMenu.configure(background="#d9d9d9")
        self.typeSelMenu.configure(highlightbackground="#d3d3d3")
        self.typeSelMenu.configure(foreground="#000000")
        self.typeSelMenu.configure(activebackground="#a7a7a7")
        self.typeSelMenu.configure(activeforeground="#000000")

        self.lblCateg = tk.Label(self.frameBody)
        self.lblCateg.place(relx=0.05, rely=0.127, height=21, width=92)
        self.lblCateg.configure(activebackground="#f9f9f9")
        self.lblCateg.configure(activeforeground="black")
        self.lblCateg.configure(anchor='w')
        self.lblCateg.configure(background="#d9d9d9")
        self.lblCateg.configure(disabledforeground="#a3a3a3")
        self.lblCateg.configure(foreground="#000000")
        self.lblCateg.configure(highlightbackground="#d9d9d9")
        self.lblCateg.configure(highlightcolor="black")
        self.lblCateg.configure(text='''Category:''')
        
        self.selCat=StringVar()
        self.selCat.set("Please select")
        self.catSelMenu = OptionMenu(self.frameBody, self.selCat, None)
        self.catSelMenu.place(relx=0.3, rely=0.127,height=21, relwidth=0.596)
        self.catSelMenu.configure(background="#d9d9d9")
        self.catSelMenu.configure(highlightbackground="#d3d3d3")
        self.catSelMenu.configure(foreground="#000000")
        self.catSelMenu.configure(activebackground="#a7a7a7")
        self.catSelMenu.configure(activeforeground="#000000")

        self.lblName = tk.Label(self.frameBody)
        self.lblName.place(relx=0.05, rely=0.2, height=21, width=92)
        self.lblName.configure(activebackground="#f9f9f9")
        self.lblName.configure(activeforeground="black")
        self.lblName.configure(anchor='w')
        self.lblName.configure(background="#d9d9d9")
        self.lblName.configure(disabledforeground="#a3a3a3")
        self.lblName.configure(foreground="#000000")
        self.lblName.configure(highlightbackground="#d9d9d9")
        self.lblName.configure(highlightcolor="black")
        self.lblName.configure(text='''Name:''')

        self.lblValue = tk.Label(self.frameBody)
        self.lblValue.place(relx=0.05, rely=0.273, height=21, width=92)
        self.lblValue.configure(activebackground="#f9f9f9")
        self.lblValue.configure(activeforeground="black")
        self.lblValue.configure(anchor='w')
        self.lblValue.configure(background="#d9d9d9")
        self.lblValue.configure(disabledforeground="#a3a3a3")
        self.lblValue.configure(foreground="#000000")
        self.lblValue.configure(highlightbackground="#d9d9d9")
        self.lblValue.configure(highlightcolor="black")
        self.lblValue.configure(text='''Value:''')

        self.lblUsername = tk.Label(self.frameBody)
        self.lblUsername.place(relx=0.05, rely=0.351, height=21, width=92)
        self.lblUsername.configure(activebackground="#f9f9f9")
        self.lblUsername.configure(activeforeground="black")
        self.lblUsername.configure(anchor='w')
        self.lblUsername.configure(background="#d9d9d9")
        self.lblUsername.configure(disabledforeground="#a3a3a3")
        self.lblUsername.configure(foreground="#000000")
        self.lblUsername.configure(highlightbackground="#d9d9d9")
        self.lblUsername.configure(highlightcolor="black")
        self.lblUsername.configure(text='''Username:''')

        self.lblEmail = tk.Label(self.frameBody)
        self.lblEmail.place(relx=0.05, rely=0.491, height=21, width=92)
        self.lblEmail.configure(activebackground="#f9f9f9")
        self.lblEmail.configure(activeforeground="black")
        self.lblEmail.configure(anchor='w')
        self.lblEmail.configure(background="#d9d9d9")
        self.lblEmail.configure(disabledforeground="#a3a3a3")
        self.lblEmail.configure(foreground="#000000")
        self.lblEmail.configure(highlightbackground="#d9d9d9")
        self.lblEmail.configure(highlightcolor="black")
        self.lblEmail.configure(text='''E-mail:''')

        self.lblDesc = tk.Label(self.frameBody)
        self.lblDesc.place(relx=0.043, rely=0.564, height=21, width=76)
        self.lblDesc.configure(activebackground="#f9f9f9")
        self.lblDesc.configure(activeforeground="black")
        self.lblDesc.configure(anchor='w')
        self.lblDesc.configure(background="#d9d9d9")
        self.lblDesc.configure(disabledforeground="#a3a3a3")
        self.lblDesc.configure(foreground="#000000")
        self.lblDesc.configure(highlightbackground="#d9d9d9")
        self.lblDesc.configure(highlightcolor="black")
        self.lblDesc.configure(text='''Description:''')

        self.entryName = tk.Entry(self.frameBody)
        self.entryName.place(relx=0.3, rely=0.2,height=21, relwidth=0.596)
        self.entryName.configure(background="white")
        self.entryName.configure(disabledforeground="#a3a3a3")
        self.entryName.configure(font="TkFixedFont")
        self.entryName.configure(foreground="#000000")
        self.entryName.configure(highlightbackground="#d9d9d9")
        self.entryName.configure(highlightcolor="black")
        self.entryName.configure(insertbackground="black")
        self.entryName.configure(selectbackground="#c4c4c4")
        self.entryName.configure(selectforeground="black")

        self.entryValue = tk.Entry(self.frameBody)
        self.entryValue.place(relx=0.3, rely=0.273,height=21, relwidth=0.596)
        self.entryValue.configure(background="white")
        self.entryValue.configure(disabledforeground="#a3a3a3")
        self.entryValue.configure(font="TkFixedFont")
        self.entryValue.configure(foreground="#000000")
        self.entryValue.configure(highlightbackground="#d9d9d9")
        self.entryValue.configure(highlightcolor="black")
        self.entryValue.configure(insertbackground="black")
        self.entryValue.configure(selectbackground="#c4c4c4")
        self.entryValue.configure(selectforeground="black")
        self.entryValue.configure(show="*")

        self.entryUsername = tk.Entry(self.frameBody)
        self.entryUsername.place(relx=0.304, rely=0.351, height=21
                , relwidth=0.596)
        self.entryUsername.configure(background="white")
        self.entryUsername.configure(disabledforeground="#a3a3a3")
        self.entryUsername.configure(font="TkFixedFont")
        self.entryUsername.configure(foreground="#000000")
        self.entryUsername.configure(highlightbackground="#d9d9d9")
        self.entryUsername.configure(highlightcolor="black")
        self.entryUsername.configure(insertbackground="black")
        self.entryUsername.configure(selectbackground="#c4c4c4")
        self.entryUsername.configure(selectforeground="black")
        self.entryUsername.configure(state="disabled")

        self.entryEmail = tk.Entry(self.frameBody)
        self.entryEmail.place(relx=0.304, rely=0.491,height=21, relwidth=0.596)
        self.entryEmail.configure(background="white")
        self.entryEmail.configure(disabledforeground="#a3a3a3")
        self.entryEmail.configure(font="TkFixedFont")
        self.entryEmail.configure(foreground="#000000")
        self.entryEmail.configure(highlightbackground="#d9d9d9")
        self.entryEmail.configure(highlightcolor="black")
        self.entryEmail.configure(insertbackground="black")
        self.entryEmail.configure(selectbackground="#c4c4c4")
        self.entryEmail.configure(selectforeground="black")
        self.entryEmail.configure(state="disabled")

        self.textDesc = tk.Text(self.frameBody)
        self.textDesc.place(relx=0.304, rely=0.564, relheight=0.189    
                    , relwidth=0.596)
        self.textDesc.configure(background="white")
        self.textDesc.configure(font="TkTextFont")
        self.textDesc.configure(foreground="black")
        self.textDesc.configure(highlightbackground="#d9d9d9")
        self.textDesc.configure(highlightcolor="black")
        self.textDesc.configure(insertbackground="black")
        self.textDesc.configure(selectbackground="#c4c4c4")
        self.textDesc.configure(selectforeground="black")
        self.textDesc.configure(wrap="word")

        self.btnCreate = tk.Button(self.frameBody)
        self.btnCreate.place(relx=0.674, rely=0.782, height=25, width=99)
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
        self.btnCancel.place(relx=0.435, rely=0.782, height=25, width=99)
        self.btnCancel.configure(activebackground="#ececec")
        self.btnCancel.configure(activeforeground="#000000")
        self.btnCancel.configure(background="#d9d9d9")
        self.btnCancel.configure(disabledforeground="#a3a3a3")
        self.btnCancel.configure(foreground="#000000")
        self.btnCancel.configure(highlightbackground="#d9d9d9")
        self.btnCancel.configure(highlightcolor="black")
        self.btnCancel.configure(pady="0")
        self.btnCancel.configure(text='''Cancel''')
        
        self.chDfEmVal = tk.IntVar()
        self.checkDefEmail = tk.Checkbutton(self.frameBody)
        self.checkDefEmail.place(relx=0.3, rely=0.431, relheight=0.038
                , relwidth=0.548)
        self.checkDefEmail.configure(activebackground="#ececec")
        self.checkDefEmail.configure(activeforeground="#000000")
        self.checkDefEmail.configure(anchor='w')
        self.checkDefEmail.configure(background="#d9d9d9")
        self.checkDefEmail.configure(disabledforeground="#a3a3a3")
        self.checkDefEmail.configure(foreground="#000000")
        self.checkDefEmail.configure(highlightbackground="#d9d9d9")
        self.checkDefEmail.configure(highlightcolor="black")
        self.checkDefEmail.configure(justify='left')
        self.checkDefEmail.configure(text='''Use default e-mail''')
        self.checkDefEmail.configure(variable=self.chDfEmVal)
        self.checkDefEmail.configure(state='disabled')
        
        self.lblMsg = tk.Label(self.frameBody)    
        self.lblMsg.place(relx=0.022, rely=0.873, height=18, width=426)
        self.lblMsg.configure(background="#d9d9d9")
        self.lblMsg.configure(disabledforeground="#a3a3a3")
        self.lblMsg.configure(foreground="#ff0000")
        
        set_icon()

if __name__ == '__main__':
    vp_start_gui()


def get_center_points(width, height):
    center_x = int((rt.winfo_screenwidth()/2) - (width/2))
    center_y = int((rt.winfo_screenheight()/2) - (height/2))
    return (center_x, center_y)

def set_icon():
    try:
        if (platform.system() == 'Linux'):
            w.iconbitmap('@' + os.path.join(os.path.dirname(__file__), '../../resources/padlock.xbm'))
        else:
            w.iconbitmap('@'+os.path.join(os.path.dirname(__file__), '../../resources/padlock.ico'))
    except:
        print("Unable to load logo image")
