"""
A module which contains util methods for other GUI modules

Created on Apr 18, 2020
@author: nenad.dramicanin
"""

import platform
import os
import tkinter
from typing import Tuple

import model.util as util
import logging
from tkinter import messagebox

ICON_DIR = 'resources'
ICON_NAME = 'padlock'
ICON_LINUX_EXT = 'png'
ICON_WIN_EXT = 'ico'

_APP_VERSION = "1.2.0"
_APP_NAME = "Password Manager"


def get_icon_ext():
    """Returns icon's extension based on a platform (OS)"""
    return ICON_LINUX_EXT if platform.system() == 'Linux' else ICON_WIN_EXT


def get_icon_path():
    """Creates absolute path to the app/form icon"""

    try:
        return os.path.join(util.get_root_path(), ICON_DIR, ICON_NAME + "." + get_icon_ext())

    except Exception as e:
        print(e)
        return None


def get_center_points(root: tkinter.Tk, width: int, height: int) -> Tuple[int, int]:
    """Calculates center points for the provided form based on it's width and height.
        The points are used as a starting points of the form, i.e. the form will be centered
    """

    center_x = int((root.winfo_screenwidth()/4) - (width/2))
    center_y = int((root.winfo_screenheight()/2) - (height/2))
    return center_x, center_y


def handle_app_exception(exc_type: str, exc_value: str, exc_traceback: str):
    """Logs exception into a log file and displays a window with a generic error message"""

    logging.basicConfig(filename='error.log', level=logging.DEBUG, format="%(asctime)s:%(message)s")
    logging.error("ERROR:", exc_info=(exc_type, exc_value, exc_traceback))
    messagebox.showerror('Error', 'An error occurred during action execution!')

def get_app_name():
    """Returns App's name"""
    return _APP_NAME

def get_app_version():
    """Returns App's version"""
    return _APP_VERSION