'''
Created on Jan 20, 2020

@author: nenad
'''

from model.data_model import Category, Entry
from pathlib import Path
from os.path import os
import jsonpickle
from model import settings, util

__CATEGORY_FILE = '.categories.json'
__ENTRY_FILE = '.entries.json'


def category_add(name, description):
    
    cat_id = settings.get_next_category_id()
    cat_id = int(cat_id) if cat_id else 1  
    category = Category(cat_id, name, description, util.get_current_date())
    
    categories = category_list()
    categories.append(category)
        
    with open(__CATEGORY_FILE, 'w') as file:
        file.write(jsonpickle.encode(categories))

    settings.set_next_entity_id(cat_id + 1)

def category_edit(edited_cat):
    categories = category_list()
    for category in categories:
        if(category.entity_id == edited_cat.entity_id):
            edited_cat.modified_date = util.get_current_date()
            categories.remove(category)
            categories.append(edited_cat)
            break   
    
    with open(__CATEGORY_FILE, 'w') as file:
        file.write(jsonpickle.encode(categories))
    
def category_delete(cat_id):
    categories = category_list()
    for category in categories:
        if(category.entity_id == cat_id):
            categories.remove(category)
            break   
    
    with open(__CATEGORY_FILE, 'w') as file:
        file.write(jsonpickle.encode(categories))

def category_list():
    if Path(__CATEGORY_FILE).is_file() and os.stat(__CATEGORY_FILE).st_size != 0:
        with open(__CATEGORY_FILE, 'r') as file:
            return jsonpickle.decode(file.read())
    else:
        return []
    
def category_get_by_name(name):
    for category in category_list():
        if(category.name == name):
            return category
        
def category_get_by_id(cat_id):
    for category in category_list():
        if(category.entity_id == cat_id):
            return category

def entry_add(name, value, entry_type, category, description, username, email):
    category_id = category_get_by_name(category).entity_id
    ent_id = settings.get_next_category_id()
    ent_id = int(ent_id) if ent_id else 1 
    entry = Entry(ent_id, name, value, entry_type, category_id, description, util.get_current_date(), username, email)
    
    entries = entry_list()
    entries.append(entry)
        
    with open(__ENTRY_FILE, 'w') as file:
        file.write(jsonpickle.encode(entries))

    settings.set_next_category_id(ent_id + 1)

def entry_list():
    if Path(__ENTRY_FILE).is_file() and os.stat(__ENTRY_FILE).st_size != 0:
        with open(__ENTRY_FILE, 'r') as file:
            return jsonpickle.decode(file.read())
    else:
        return []

def entry_edit(edited_entry):
    entries = entry_list()
    for entry in entries:
        if(entry.entity_id == edited_entry.entity_id):
            entries.remove(entry)
            entries.append(edited_entry)
            break   
    
    with open(__ENTRY_FILE, 'w') as file:
        file.write(jsonpickle.encode(entries))

def entry_delete(entry_id):
    entries = entry_list()
    for entry in entries:
        if(entry.entity_id == entry_id):
            entries.remove(entry)
            break   
    
    with open(__ENTRY_FILE, 'w') as file:
        file.write(jsonpickle.encode(entries))

def entry_get_by_id(entry_id):
    for entry in entry_list():
        if(entry.entity_id == entry_id):
            return entry

def entry_delete_all():
    if Path(__ENTRY_FILE).is_file() and os.stat(__ENTRY_FILE).st_size != 0:
        with open(__ENTRY_FILE, 'w') as file:
            file.write("[]")   
      
def category_delete_all():
    if Path(__CATEGORY_FILE).is_file() and os.stat(__CATEGORY_FILE).st_size != 0:
        with open(__CATEGORY_FILE, 'w') as file:
            file.write("[]")


def entity_search(search_ctg, search_type, search_name):
    result = []
    cat_id = None if search_ctg is None else category_get_by_name(search_ctg).entity_id
    for entry in entry_list():
        if((cat_id is None or entry.category_id == cat_id) and
            (search_type is None or entry.entry_type == search_type) and
            (search_name is None or search_name.lower() in entry.name.lower())):
            result.append(entry)
    return result;
