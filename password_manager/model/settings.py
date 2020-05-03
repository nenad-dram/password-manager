"""
Module responsible for handling settings file with non-model data

Created on Jan 26, 2020
@author: nenad.dramicanin
"""

import configparser
from typing import Optional

from . import util, services

# Constants
__APP_SETTINGS = 'APP SETTINGS'
__DATA_CONFIG_FILE = util.get_root_path() + '/data/data.ini'
__NEXT_CAT_ID_KEY = 'next_category_id'
__NEXT_ENT_ID_KEY = 'next_entry_id'
__DEFAULT_EMAIL__KEY = 'default_email'
__MASTER_PWD_KEY = 'master_password'

# List of available settings
__all_settings = [__NEXT_CAT_ID_KEY, __NEXT_ENT_ID_KEY, __DEFAULT_EMAIL__KEY, __MASTER_PWD_KEY]


def init():
    """Initialisation of settings file

    Implies creating 'data' dir to store all application files, and creating settings file with all parameters
    set to empty string
    """

    services.make_data_dir()
    config = configparser.ConfigParser()
    config.add_section(__APP_SETTINGS)
    for key in __all_settings:
        config[__APP_SETTINGS][key] = ""
    with open(__DATA_CONFIG_FILE, 'w+') as configfile:
        config.write(configfile)


def __get(key: str) -> Optional[str]:
    """Returns setting with given key, if exists"""

    config = configparser.ConfigParser()
    config.read(__DATA_CONFIG_FILE)
    if config.has_option(__APP_SETTINGS, key):
        return config[__APP_SETTINGS][key]
    else:
        return None


def __save(key: str, value: str):
    """Saves setting with given key value pair"""

    config = configparser.ConfigParser()
    if not config.read(__DATA_CONFIG_FILE):
        config.add_section(__APP_SETTINGS)
    config[__APP_SETTINGS][key] = value
    with open(__DATA_CONFIG_FILE, 'w+') as configfile:
        config.write(configfile)


def get_master_password() -> str:
    """Returns master password"""

    return __get(__MASTER_PWD_KEY)


def set_master_password(password: str):
    """Saves master password"""

    __save(__MASTER_PWD_KEY, password)


def set_default_email(email: str):
    """Saves default email"""

    __save(__DEFAULT_EMAIL__KEY, email)


def get_default_email() -> str:
    """Returns default e-mail value"""

    return __get(__DEFAULT_EMAIL__KEY)


def get_next_category_id() -> str:
    """Returns value for next category ID"""

    return __get(__NEXT_CAT_ID_KEY)


def set_next_category_id(cat_id: str):
    """Saves value for next category ID"""

    __save(__NEXT_CAT_ID_KEY, str(cat_id))


def get_next_entity_id() -> str:
    """Returns value for next entity ID"""

    return __get(__NEXT_CAT_ID_KEY)


def set_next_entity_id(ent_id: str):
    """Saves value for next entity ID"""

    __save(__NEXT_CAT_ID_KEY, str(ent_id))