"""
Module which contains all model classes.

Category and Entry classes inherits Base class which contains common attributes.
Enum is defined to represent Entry type.

Created on Jan 20, 2020
@author: nenad.dramicanin
"""
from enum import Enum


class Base(object):

    def __init__(self, entity_id, name, description, modified_date):
        self.entity_id = entity_id
        self.name = name
        self.description = description
        self.modified_date = modified_date


class Category(Base):
    
    def __init__(self, entity_id, name, description, modified_date):
        super(Category, self).__init__(entity_id, name, description, modified_date)


class Entry(Base):

    def __init__(self, entity_id, name, value, entry_type, category_id, description, modified_date, username=None, email=None):
        super(Entry, self).__init__(entity_id, name, description, modified_date)
        self.category_id = category_id
        self.entry_type = entry_type
        self.value = value
        self.username = username
        self.email = email


class EntryType(Enum):
    SECRET = "secret"
    ACCOUNT = "account"
