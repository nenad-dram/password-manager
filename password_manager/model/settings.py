'''
Created on Feb 26, 2020

@author: ndramica
'''
import configparser
import os

__APP_SETTINGS = 'APP SETTINGS'
__DATA_CONFIG_FILE = os.path.join(os.path.dirname(__file__), '../../data/data.ini')

__NEXT_CAT_ID_KEY = 'next_category_id'
__NEXT_ENT_ID_KEY = 'next_entry_id'
__DEFAULT_EMAIL__KEY = 'default_email'
__MASTER_PWD_KEY = 'master_password'

__all_settings = [__NEXT_CAT_ID_KEY, __NEXT_ENT_ID_KEY, __DEFAULT_EMAIL__KEY, __MASTER_PWD_KEY]

def init():
    config = configparser.ConfigParser()
    config.add_section(__APP_SETTINGS)
    open(__DATA_CONFIG_FILE, 'w')
    for key in __all_settings:
        config[__APP_SETTINGS][key] = ""
    with open(__DATA_CONFIG_FILE, 'w') as configfile:
        config.write(configfile)

def __get(key):
    config = configparser.ConfigParser()
    config.read(__DATA_CONFIG_FILE)
    if config.has_option(__APP_SETTINGS, key):
        return config[__APP_SETTINGS][key]
    else:
        return None
    
def __save(key, value):
    config = configparser.ConfigParser()
    if not config.read(__DATA_CONFIG_FILE):
        config.add_section(__APP_SETTINGS)
    config[__APP_SETTINGS][key] = value
    with open(__DATA_CONFIG_FILE, 'w') as configfile:
        config.write(configfile)

def get_master_password():
    return __get(__MASTER_PWD_KEY)

def set_master_password(password):
    __save(__MASTER_PWD_KEY, password)

def set_default_email(email):
    __save(__DEFAULT_EMAIL__KEY, email)

def get_default_email():
    return __get(__DEFAULT_EMAIL__KEY)

def get_next_category_id():
    return __get(__NEXT_CAT_ID_KEY)

def set_next_category_id(cat_id):
    __save(__NEXT_CAT_ID_KEY, str(cat_id))
    
def get_next_entity_id():
    return __get(__NEXT_CAT_ID_KEY)

def set_next_entity_id(ent_id):
    __save(__NEXT_CAT_ID_KEY, str(ent_id))