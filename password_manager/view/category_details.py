#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.26
#  in conjunction with Tcl version 8.6
#    Feb 05, 2020 10:33:21 AM CET  platform: Windows NT

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

from support import category_details_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = CategoryDetailsWindow (root)
    category_details_support.init(root, top)
    root.mainloop()

    w = None
def create_CategoryDetailsWindow(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    top = CategoryDetailsWindow (w)
    category_details_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_CategoryNewWindow():
    global w
    w.destroy()
    w = None

class CategoryDetailsWindow:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        
        width = 355
        height = 432
        
        center = get_center_points(width, height)
        
        top.geometry("{}x{}+{}+{}".format(width, height, center[0], center[1]))

        top.minsize(176, 1)
        top.maxsize(3844, 1061)
        top.resizable(1, 1)
        top.title("Category Details")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")
        top.grab_set()

        self.frameBody = tk.Frame(top)
        self.frameBody.place(relx=0.0, rely=0.0, relheight=1.007, relwidth=1.003)

        self.frameBody.configure(relief='groove')
        self.frameBody.configure(borderwidth="2")
        self.frameBody.configure(relief="groove")
        self.frameBody.configure(background="#d9d9d9")
        self.frameBody.configure(highlightbackground="#d9d9d9")
        self.frameBody.configure(highlightcolor="black")

        self.entName = tk.Entry(self.frameBody)
        self.entName.place(relx=0.338, rely=0.184,height=20, relwidth=0.577)
        self.entName.configure(background="white")
        self.entName.configure(disabledforeground="#a3a3a3")
        self.entName.configure(font="TkFixedFont")
        self.entName.configure(foreground="#000000")
        self.entName.configure(highlightbackground="#d9d9d9")
        self.entName.configure(highlightcolor="black")
        self.entName.configure(insertbackground="black")
        self.entName.configure(selectbackground="#c4c4c4")
        self.entName.configure(selectforeground="black")

        self.lblName = tk.Label(self.frameBody)
        self.lblName.place(relx=0.141, rely=0.184, height=21, width=54)
        self.lblName.configure(activebackground="#f9f9f9")
        self.lblName.configure(activeforeground="black")
        self.lblName.configure(background="#d9d9d9")
        self.lblName.configure(disabledforeground="#a3a3a3")
        self.lblName.configure(foreground="#000000")
        self.lblName.configure(highlightbackground="#d9d9d9")
        self.lblName.configure(highlightcolor="black")
        self.lblName.configure(text='''Name:''')

        self.lblDescription = tk.Label(self.frameBody)
        self.lblDescription.place(relx=0.028, rely=0.253, height=21, width=76)
        self.lblDescription.configure(activebackground="#f9f9f9")
        self.lblDescription.configure(activeforeground="black")
        self.lblDescription.configure(background="#d9d9d9")
        self.lblDescription.configure(disabledforeground="#a3a3a3")
        self.lblDescription.configure(foreground="#000000")
        self.lblDescription.configure(highlightbackground="#d9d9d9")
        self.lblDescription.configure(highlightcolor="black")
        self.lblDescription.configure(text='''Description:''')

        self.txtDescripton = tk.Text(self.frameBody)
        self.txtDescripton.place(relx=0.338, rely=0.276, relheight=0.423
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

        self.btnCancel = tk.Button(self.frameBody)
        self.btnCancel.place(relx=0.451, rely=0.828, height=24, width=77)
        self.btnCancel.configure(activebackground="#ececec")
        self.btnCancel.configure(activeforeground="#000000")
        self.btnCancel.configure(background="#d9d9d9")
        self.btnCancel.configure(disabledforeground="#a3a3a3")
        self.btnCancel.configure(foreground="#000000")
        self.btnCancel.configure(highlightbackground="#d9d9d9")
        self.btnCancel.configure(highlightcolor="black")
        self.btnCancel.configure(pady="0")
        self.btnCancel.configure(text='''Cancel''')

        self.lblId = tk.Label(self.frameBody)
        self.lblId.place(relx=0.197, rely=0.069, height=18, width=21)
        self.lblId.configure(background="#d9d9d9")
        self.lblId.configure(disabledforeground="#a3a3a3")
        self.lblId.configure(foreground="#000000")
        self.lblId.configure(text='''ID:''')

        self.entId = tk.Entry(self.frameBody)
        self.entId.place(relx=0.338, rely=0.092,height=20, relwidth=0.577)
        self.entId.configure(background="white")
        self.entId.configure(disabledforeground="#a3a3a3")
        self.entId.configure(font="TkFixedFont")
        self.entId.configure(foreground="#000000")
        self.entId.configure(highlightbackground="#d9d9d9")
        self.entId.configure(highlightcolor="black")
        self.entId.configure(insertbackground="black")
        self.entId.configure(selectbackground="#c4c4c4")
        self.entId.configure(selectforeground="black")

        self.entModDate = tk.Entry(self.frameBody)
        self.entModDate.place(relx=0.338, rely=0.749,height=20, relwidth=0.577)
        self.entModDate.configure(background="white")
        self.entModDate.configure(disabledforeground="#a3a3a3")
        self.entModDate.configure(font="TkFixedFont")
        self.entModDate.configure(foreground="#000000")
        self.entModDate.configure(highlightbackground="#d9d9d9")
        self.entModDate.configure(highlightcolor="black")
        self.entModDate.configure(insertbackground="black")
        self.entModDate.configure(selectbackground="#c4c4c4")
        self.entModDate.configure(selectforeground="black")

        self.lblModDate = tk.Label(self.frameBody)
        self.lblModDate.place(relx=0.085, rely=0.749, height=21, width=74)
        self.lblModDate.configure(activebackground="#f9f9f9")
        self.lblModDate.configure(activeforeground="black")
        self.lblModDate.configure(background="#d9d9d9")
        self.lblModDate.configure(disabledforeground="#a3a3a3")
        self.lblModDate.configure(foreground="#000000")
        self.lblModDate.configure(highlightbackground="#d9d9d9")
        self.lblModDate.configure(highlightcolor="black")
        self.lblModDate.configure(text='''Modified:''')

        self.btnSave = tk.Button(self.frameBody)
        self.btnSave.place(relx=0.704, rely=0.828, height=24, width=77)
        self.btnSave.configure(activebackground="#ececec")
        self.btnSave.configure(activeforeground="#000000")
        self.btnSave.configure(background="#d9d9d9")
        self.btnSave.configure(disabledforeground="#a3a3a3")
        self.btnSave.configure(foreground="#000000")
        self.btnSave.configure(highlightbackground="#d9d9d9")
        self.btnSave.configure(highlightcolor="black")
        self.btnSave.configure(pady="0")
        self.btnSave.configure(text='''Save''')
    
        self.lblMsg = tk.Label(self.frameBody)    
        self.lblMsg.place(relx=0.028, rely=0.92, height=18, width=336)    
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
            root.iconbitmap('@../resources/padlock.xbm')
        else:
            root.iconbitmap('../resources/padlock.ico')
    except:
        print("Unable to load logo image")
