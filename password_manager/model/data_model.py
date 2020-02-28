'''
Created on Jan 20, 2020

@author: nenad
'''
from enum import Enum

class Base(object):

    def __init__(self, entity_id, name, description, modifed_date):
        self.entity_id = entity_id
        self.name = name
        self.description = description
        self.modified_date = modifed_date

class Category(Base):
    
    def __init__(self, entity_id, name, description, modifed_date):
        super(Category, self).__init__(entity_id, name, description, modifed_date)

class Entry(Base):

    def __init__(self, entity_id, name, value, entry_type, category_id, description, modifed_date, username=None, email=None):
        super(Entry, self).__init__(entity_id, name, description, modifed_date)
        self.category_id = category_id
        self.entry_type = entry_type
        self.value = value
        self.username = username
        self.email = email

class EntryType(Enum):
    SECRET = "secret"
    ACCOUNT = "account"
