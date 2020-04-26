import platform
import os
from model import util

ICON_DIR = 'resources'
ICON_NAME = 'padlock'
ICON_LINUX_EXT = 'xbm'
ICON_WIN_EXT = 'ico'


def get_icon_ext():
    return ICON_LINUX_EXT if platform.system() == 'Linux' else ICON_WIN_EXT


def get_icon_path(for_main=False):
    try:
        return '@' + os.path.join(util.get_root_path(), ICON_DIR, ICON_NAME + "." + get_icon_ext())

    except Exception as e:
        # print("Unable to load logo image")
        print(e)
        return None


def get_center_points(root, width, height):
    center_x = int((root.winfo_screenwidth()/2) - (width/2))
    center_y = int((root.winfo_screenheight()/2) - (height/2))
    return center_x, center_y
