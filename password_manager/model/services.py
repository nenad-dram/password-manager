'''
Created on Jan 20, 2020

@author: nenad
'''

from model.data_model import Category, Entry
from pathlib import Path
import os
from model import settings, util, security
import jsonpickle

__CATEGORY_FILE = os.path.join(os.path.dirname(__file__), '../../data/categories.json')
__ENTRY_FILE = os.path.join(os.path.dirname(__file__), '../../data/entries')

category_list_cache = []
entry_list_cache = []


def category_add(name, description):
    
    cat_id = settings.get_next_category_id()
    cat_id = int(cat_id) if cat_id else 1  
    category = Category(cat_id, name, description, util.get_current_date())
    
    category_list_cache.append(category)

    with open(__CATEGORY_FILE, 'w') as file:
        file.write(jsonpickle.encode(category_list_cache))

    settings.set_next_entity_id(cat_id + 1)


def category_edit(edited_cat):
    for index, category in enumerate(category_list_cache):
        if category.entity_id == edited_cat.entity_id:
            edited_cat.modified_date = util.get_current_date()
            category_list_cache[index] = edited_cat
            break   
    
    with open(__CATEGORY_FILE, 'w') as file:
        file.write(jsonpickle.encode(category_list_cache))


def category_delete(cat_id):
    categories = category_list()
    for category in categories:
        if category.entity_id == cat_id:
            category_list_cache.remove(category)
            break   
    
    with open(__CATEGORY_FILE, 'w') as file:
        file.write(jsonpickle.encode(category_list_cache))


def category_list():
    global category_list_cache
    if len(category_list_cache) == 0 and util.file_exists_and_not_empty(__CATEGORY_FILE):
        with open(__CATEGORY_FILE, 'r') as file:
            category_list_cache = jsonpickle.decode(file.read())
    return category_list_cache


def category_get_by_name(name):
    for category in category_list():
        if category.name == name:
            return category


def category_get_by_id(cat_id):
    for category in category_list():
        if category.entity_id == cat_id:
            return category


def entry_add(name, value, entry_type, category, description, username, email):
    category_id = category_get_by_name(category).entity_id
    ent_id = settings.get_next_category_id()
    ent_id = int(ent_id) if ent_id else 1 
    entry = Entry(ent_id, name, value, entry_type, category_id, description, util.get_current_date(), username, email)
    
    entries = entry_list()
    entries.append(entry)

    encrypt_and_save(__ENTRY_FILE, jsonpickle.encode(entries))

    settings.set_next_category_id(ent_id + 1)


def entry_list():
    global entry_list_cache

    if len(entry_list_cache) == 0 and util.file_exists_and_not_empty(__ENTRY_FILE):
        entry_list_cache = jsonpickle.decode(read_and_decrypt(__ENTRY_FILE))

    return entry_list_cache


def entry_edit(edited_entry):
    entries = entry_list()
    for entry in entries:
        if entry.entity_id == edited_entry.entity_id:
            edited_entry.modified_date = util.get_current_date()
            entries.remove(entry)
            entries.append(edited_entry)
            break

    encrypt_and_save(__ENTRY_FILE, jsonpickle.encode(entries))


def entry_delete(entry_id):
    entries = entry_list()
    for entry in entries:
        if entry.entity_id == entry_id:
            entries.remove(entry)
            break

    encrypt_and_save(__ENTRY_FILE, jsonpickle.encode(entries))


def entry_get_by_id(entry_id):
    for entry in entry_list():
        if entry.entity_id == entry_id:
            return entry


def entry_delete_all():
    global entry_list_cache
    entry_list_cache = []
    encrypt_and_save(__ENTRY_FILE, str(entry_list_cache))


def category_delete_all():
    global category_list_cache
    category_list_cache = []
    if util.file_exists_and_not_empty(__CATEGORY_FILE):
        with open(__CATEGORY_FILE, 'w') as file:
            file.write(str(category_list_cache))


def entity_search(search_ctg, search_type, search_name):
    result = []
    cat_id = None if search_ctg is None else category_get_by_name(search_ctg).entity_id
    for entry in entry_list():
        if(cat_id is None or entry.category_id == cat_id) and \
                (search_type is None or entry.entry_type == search_type) and \
                (search_name is None or search_name.lower() in entry.name.lower()):
            result.append(entry)
    return result


def encrypt_and_save(file_name, content):
    with open(file_name, 'w') as file:
        encrypted_content = security.encrypt_data(content)
        file.write(encrypted_content.decode('utf-8'))


def read_and_decrypt(file_name):
    if util.file_exists_and_not_empty(file_name):
        with open(file_name, 'r') as file:
            return security.decrypt_data(file.read().encode())
