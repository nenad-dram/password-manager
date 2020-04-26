#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 5.0.1
#  in conjunction with Tcl version 8.6
#    Feb 16, 2020 11:30:55 AM CET  platform: Linux

import sys
import tkinter as tk
import support.entry_details_support as entry_details_support
import view.window_util as window_util
from tkinter import ttk


def create_entry_details_window(root, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_EntryDetailsWidnow(root, *args, **kwargs)' .'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel(root)
    top = EntryDetailsWindow(w)
    entry_details_support.init(w, top, *args, **kwargs)
    return w, top


def destroy_entry_details_window():
    global w
    w.destroy()
    w = None


class EntryDetailsWindow:
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
        
        width = 470
        height = 551
        
        center = window_util.get_center_points(top, width, height)
        
        top.geometry("{}x{}+{}+{}".format(width, height, center[0], center[1]))
        
        top.minsize(176, 1)
        top.maxsize(5764, 1590)
        top.title("Entry Details")
        top.configure(highlightcolor="black")

        top.iconbitmap(window_util.get_icon_path())

        self.frameBody = tk.Frame(top)
        self.frameBody.place(relx=0.0, rely=0.0, relheight=1.0, relwidth=1.0)
        self.frameBody.configure(borderwidth="2")
        self.frameBody.configure(relief="groove")
        self.frameBody.configure(background="#d9d9d9")
        self.frameBody.configure(highlightbackground="#d9d9d9")
        self.frameBody.configure(highlightcolor="black")

        self.lblType = tk.Label(self.frameBody)
        self.lblType.place(relx=0.033, rely=0.127, height=21, width=91)
        self.lblType.configure(activebackground="#f9f9f9")
        self.lblType.configure(anchor='w')
        self.lblType.configure(text='''Type:''')
        self.lblType.configure(background="#d9d9d9")
        self.lblType.configure(highlightbackground="#d9d9d9")
        self.lblType.configure(highlightcolor=_fgcolor)
        self.lblType.configure(foreground=_fgcolor)

        self.selType = tk.StringVar()
        self.typeSelMenu = tk.OptionMenu(self.frameBody, self.selType, None)
        self.typeSelMenu.place(relx=0.219, rely=0.127, height=21, relwidth=0.6)
        self.typeSelMenu.configure(background="#d9d9d9")
        self.typeSelMenu.configure(highlightbackground="#d3d3d3")
        self.typeSelMenu.configure(foreground=_fgcolor)
        self.typeSelMenu.configure(activebackground="#a7a7a7")
        self.typeSelMenu.configure(activeforeground=_fgcolor)
        self.typeSelMenu.configure(disabledforeground=_fgcolor)

        self.lblCateg = tk.Label(self.frameBody)
        self.lblCateg.place(relx=0.033, rely=0.2, height=21, width=91)
        self.lblCateg.configure(activebackground="#f9f9f9")
        self.lblCateg.configure(anchor='w')
        self.lblCateg.configure(text='''Category:''')
        self.lblCateg.configure(background="#d9d9d9")
        self.lblCateg.configure(highlightbackground="#d9d9d9")
        self.lblCateg.configure(highlightcolor="black")
        self.lblCateg.configure(foreground=_fgcolor)

        self.selCat = tk.StringVar()
        self.catSelMenu = tk.OptionMenu(self.frameBody, self.selCat, None)
        self.catSelMenu.place(relx=0.219, rely=0.2, height=21, relwidth=0.6)
        self.catSelMenu.configure(background="#d9d9d9")
        self.catSelMenu.configure(highlightbackground="#d3d3d3")
        self.catSelMenu.configure(foreground=_fgcolor)
        self.catSelMenu.configure(activebackground="#a7a7a7")
        self.catSelMenu.configure(activeforeground=_fgcolor)
        self.catSelMenu.configure(disabledforeground=_fgcolor)

        self.lblName = tk.Label(self.frameBody)
        self.lblName.place(relx=0.033, rely=0.272, height=21, width=91)
        self.lblName.configure(activebackground="#f9f9f9")
        self.lblName.configure(anchor='w')
        self.lblName.configure(text='''Name:''')
        self.lblName.configure(background="#d9d9d9")
        self.lblName.configure(highlightbackground="#d9d9d9")
        self.lblName.configure(highlightcolor="black")
        self.lblName.configure(foreground=_fgcolor)

        self.lblValue = tk.Label(self.frameBody)
        self.lblValue.place(relx=0.033, rely=0.345, height=21, width=91)
        self.lblValue.configure(activebackground="#f9f9f9")
        self.lblValue.configure(anchor='w')
        self.lblValue.configure(text='''Value:''')
        self.lblValue.configure(background="#d9d9d9")
        self.lblValue.configure(highlightbackground="#d9d9d9")
        self.lblValue.configure(highlightcolor="black")
        self.lblValue.configure(foreground=_fgcolor)

        self.lblUsername = tk.Label(self.frameBody)
        self.lblUsername.place(relx=0.033, rely=0.417, height=21, width=81)
        self.lblUsername.configure(activebackground="#f9f9f9")
        self.lblUsername.configure(anchor='w')
        self.lblUsername.configure(text='''Username:''')
        self.lblUsername.configure(background="#d9d9d9")
        self.lblUsername.configure(highlightbackground="#d9d9d9")
        self.lblUsername.configure(highlightcolor="black")
        self.lblUsername.configure(foreground=_fgcolor)

        self.lblEmail = tk.Label(self.frameBody)
        self.lblEmail.place(relx=0.044, rely=0.544, height=21, width=80)
        self.lblEmail.configure(activebackground="#f9f9f9")
        self.lblEmail.configure(anchor='w')
        self.lblEmail.configure(text='''E-mail:''')
        self.lblEmail.configure(background="#d9d9d9")
        self.lblEmail.configure(highlightbackground="#d9d9d9")
        self.lblEmail.configure(highlightcolor="black")
        self.lblEmail.configure(foreground=_fgcolor)

        self.lblDesc = tk.Label(self.frameBody)
        self.lblDesc.place(relx=0.044, rely=0.617, height=21, width=79)
        self.lblDesc.configure(activebackground="#f9f9f9")
        self.lblDesc.configure(anchor='w')
        self.lblDesc.configure(text='''Description:''')
        self.lblDesc.configure(background="#d9d9d9")
        self.lblDesc.configure(highlightbackground="#d9d9d9")
        self.lblDesc.configure(highlightcolor="black")
        self.lblDesc.configure(foreground=_fgcolor)

        self.entryName = tk.Entry(self.frameBody)
        self.entryName.place(relx=0.219, rely=0.272, height=21, relwidth=0.6)
        self.entryName.configure(background="white")
        self.entryName.configure(font="TkFixedFont")
        self.entryName.configure(selectbackground="#c4c4c4")
        self.entryName.configure(foreground=_fgcolor)
        self.entryName.configure(disabledforeground=_fgcolor)
        self.entryName.configure(selectforeground=_fgcolor)

        self.entryValue = tk.Entry(self.frameBody)
        self.entryValue.place(relx=0.219, rely=0.345, height=21, relwidth=0.446)
        self.entryValue.configure(background="white")
        self.entryValue.configure(font="TkFixedFont")
        self.entryValue.configure(selectbackground="#c4c4c4")
        self.entryValue.configure(disabledforeground=_fgcolor)
        self.entryValue.configure(selectforeground=_fgcolor)
        self.entryValue.configure(foreground=_fgcolor)
        self.entryValue.configure(show="*")         

        self.entryUsername = tk.Entry(self.frameBody)
        self.entryUsername.place(relx=0.219, rely=0.417, height=21, relwidth=0.6)
        self.entryUsername.configure(foreground=_fgcolor)
        self.entryUsername.configure(background="white")
        self.entryUsername.configure(font="TkFixedFont")
        self.entryUsername.configure(selectbackground="#c4c4c4")
        self.entryUsername.configure(disabledforeground=_fgcolor)
        self.entryUsername.configure(selectforeground=_fgcolor)

        self.entryEmail = tk.Entry(self.frameBody)
        self.entryEmail.place(relx=0.219, rely=0.544, height=21, relwidth=0.6)
        self.entryEmail.configure(background="white")
        self.entryEmail.configure(font="TkFixedFont")
        self.entryEmail.configure(selectbackground="#c4c4c4")
        self.entryEmail.configure(foreground=_fgcolor)
        self.entryEmail.configure(disabledforeground=_fgcolor)
        self.entryEmail.configure(selectforeground=_fgcolor)

        self.textDesc = tk.Text(self.frameBody)
        self.textDesc.place(relx=0.219, rely=0.617, relheight=0.163, relwidth=0.6)
        self.textDesc.configure(background="white")
        self.textDesc.configure(font="TkTextFont")
        self.textDesc.configure(selectbackground="#c4c4c4")
        self.textDesc.configure(wrap="word")
        self.textDesc.configure(foreground=_fgcolor)
        self.textDesc.configure(selectforeground=_fgcolor)

        self.btnSave = tk.Button(self.frameBody)
        self.btnSave.place(relx=0.591, rely=0.853, height=25, width=98)
        self.btnSave.configure(activebackground="#ececec")
        self.btnSave.configure(activeforeground="#000000")
        self.btnSave.configure(pady="0")
        self.btnSave.configure(text='''Save''')
        self.btnSave.configure(background="#d9d9d9")
        self.btnSave.configure(highlightbackground="#d9d9d9")
        self.btnSave.configure(highlightcolor="black")
        self.btnSave.configure(foreground=_fgcolor)

        self.btnClose = tk.Button(self.frameBody)
        self.btnClose.place(relx=0.35, rely=0.853, height=25, width=99)
        self.btnClose.configure(activebackground="#ececec")
        self.btnClose.configure(activeforeground="#000000")
        self.btnClose.configure(pady="0")
        self.btnClose.configure(text='''Close''')
        self.btnClose.configure(background="#d9d9d9")
        self.btnClose.configure(highlightbackground="#d9d9d9")
        self.btnClose.configure(highlightcolor="black")
        self.btnClose.configure(foreground=_fgcolor)
        
        self.chDfEmVal = tk.IntVar()
        self.checkDefEmail = tk.Checkbutton(self.frameBody)
        self.checkDefEmail.place(relx=0.219, rely=0.49, relheight=0.038, relwidth=0.442)
        self.checkDefEmail.configure(activebackground="#d9d9d9")
        self.checkDefEmail.configure(activeforeground="black")
        self.checkDefEmail.configure(anchor='w')
        self.checkDefEmail.configure(justify='left')
        self.checkDefEmail.configure(text='''Use default e-mail''')
        self.checkDefEmail.configure(variable=self.chDfEmVal)
        self.checkDefEmail.configure(background="#d9d9d9")
        self.checkDefEmail.configure(highlightbackground="#d9d9d9")
        self.checkDefEmail.configure(highlightcolor="black")
        self.checkDefEmail.configure(foreground=_fgcolor)

        self.lblId = tk.Label(self.frameBody)
        self.lblId.place(relx=0.033, rely=0.054, height=21, width=92)
        self.lblId.configure(activebackground="#f9f9f9")
        self.lblId.configure(anchor='w')
        self.lblId.configure(text='''ID:''')
        self.lblId.configure(background="#d9d9d9")
        self.lblId.configure(highlightbackground="#d9d9d9")
        self.lblId.configure(highlightcolor="black")
        self.lblId.configure(foreground=_fgcolor)

        self.entryId = tk.Entry(self.frameBody)
        self.entryId.place(relx=0.219, rely=0.054, height=21, relwidth=0.184)
        self.entryId.configure(background="white")
        self.entryId.configure(font="TkFixedFont")
        self.entryId.configure(selectbackground="#c4c4c4")
        self.entryId.configure(foreground=_fgcolor)

        self.entryModDate = tk.Entry(self.frameBody)
        self.entryModDate.place(relx=0.219, rely=0.799, height=21, relwidth=0.6)
        self.entryModDate.configure(background="white")
        self.entryModDate.configure(font="TkFixedFont")
        self.entryModDate.configure(selectbackground="#c4c4c4")
        self.entryModDate.configure(foreground=_fgcolor)

        self.lblModDate = tk.Label(self.frameBody)
        self.lblModDate.place(relx=0.044, rely=0.799, height=21, width=65)
        self.lblModDate.configure(activebackground="#f9f9f9")
        self.lblModDate.configure(anchor='w')
        self.lblModDate.configure(text='''Modified:''')
        self.lblModDate.configure(background="#d9d9d9")
        self.lblModDate.configure(highlightbackground="#d9d9d9")
        self.lblModDate.configure(highlightcolor="black")
        self.lblModDate.configure(foreground=_fgcolor)

        self.btnDelete = tk.Button(self.frameBody)
        self.btnDelete.place(relx=0.635, rely=0.054, height=21, width=79)
        self.btnDelete.configure(activebackground="#ececec")
        self.btnDelete.configure(activeforeground="#000000")
        self.btnDelete.configure(pady="0")
        self.btnDelete.configure(text='''Delete''')
        self.btnDelete.configure(background="#d9d9d9")
        self.btnDelete.configure(highlightbackground="#d9d9d9")
        self.btnDelete.configure(highlightcolor="black")
        self.btnDelete.configure(foreground=_fgcolor)
        
        self.btnEdit = tk.Button(self.frameBody)
        self.btnEdit.place(relx=0.438, rely=0.054, height=21, width=79)
        self.btnEdit.configure(activebackground="#ececec")
        self.btnEdit.configure(activeforeground="#000000")
        self.btnEdit.configure(pady="0")
        self.btnEdit.configure(text='''Edit''')
        self.btnEdit.configure(background="#d9d9d9")
        self.btnEdit.configure(highlightbackground="#d9d9d9")
        self.btnEdit.configure(highlightcolor="black")
        self.btnEdit.configure(foreground=_fgcolor)

        self.btnCopyVal = tk.Button(self.frameBody)
        self.btnCopyVal.place(relx=0.832, rely=0.345, height=21, width=60)
        self.btnCopyVal.configure(activebackground="#ececec")
        self.btnCopyVal.configure(activeforeground="#000000")
        self.btnCopyVal.configure(pady="0")
        self.btnCopyVal.configure(text='''Copy''')
        self.btnCopyVal.configure(background="#d9d9d9")
        self.btnCopyVal.configure(highlightbackground="#d9d9d9")
        self.btnCopyVal.configure(highlightcolor="black")
        self.btnCopyVal.configure(foreground=_fgcolor)

        self.btnCopyUser = tk.Button(self.frameBody)
        self.btnCopyUser.place(relx=0.832, rely=0.417, height=21, width=60)
        self.btnCopyUser.configure(activebackground="#ececec")
        self.btnCopyUser.configure(activeforeground="#000000")
        self.btnCopyUser.configure(pady="0")
        self.btnCopyUser.configure(text='''Copy''')
        self.btnCopyUser.configure(state='disabled')
        self.btnCopyUser.configure(background="#d9d9d9")
        self.btnCopyUser.configure(highlightbackground="#d9d9d9")
        self.btnCopyUser.configure(highlightcolor="black")
        self.btnCopyUser.configure(foreground=_fgcolor)

        self.btnCopyEmail = tk.Button(self.frameBody)
        self.btnCopyEmail.place(relx=0.832, rely=0.544, height=21, width=60)
        self.btnCopyEmail.configure(activebackground="#ececec")
        self.btnCopyEmail.configure(activeforeground="#000000")
        self.btnCopyEmail.configure(pady="0")
        self.btnCopyEmail.configure(text='''Copy''')
        self.btnCopyEmail.configure(state='disabled')
        self.btnCopyEmail.configure(background="#d9d9d9")
        self.btnCopyEmail.configure(highlightbackground="#d9d9d9")
        self.btnCopyEmail.configure(highlightcolor="black")
        self.btnCopyEmail.configure(foreground=_fgcolor)
        
        self.setChBtnShow = tk.IntVar()
        self.chBtnShow = tk.Checkbutton(self.frameBody)
        self.chBtnShow.place(relx=0.678, rely=0.345, relwidth=0.133, relheight=0.0, height=18)
        self.chBtnShow.configure(variable=self.setChBtnShow)
        self.chBtnShow.configure(activebackground="#d9d9d9")
        self.chBtnShow.configure(activeforeground="black")
        self.chBtnShow.configure(anchor='w')
        self.chBtnShow.configure(justify='left')
        self.chBtnShow.configure(text='''Show''')
        self.chBtnShow.configure(background="#d9d9d9")
        self.chBtnShow.configure(highlightbackground="#d9d9d9")
        self.chBtnShow.configure(highlightcolor="black")
        self.chBtnShow.configure(foreground=_fgcolor)

        self.menubar = tk.Menu(top, font="TkMenuFont", bg=_bgcolor, fg=_fgcolor)
        top.configure(menu=self.menubar)
        
        self.lblMsg = tk.Label(self.frameBody)    
        self.lblMsg.place(relx=0.022, rely=0.935, height=18, width=436)
        self.lblMsg.configure(background="#d9d9d9")
        self.lblMsg.configure(disabledforeground="#a3a3a3")
        self.lblMsg.configure(foreground="#ff0000")