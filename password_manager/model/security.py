'''
Created on Jan 22, 2020

@author: ndramica
'''
import hashlib
import re
from model import settings, services


__SHA265_REGEX = '^[A-Fa-f0-9]{64}$'


def hash_sha256(value):
    return hashlib.sha256(value.encode('utf-8')).hexdigest()

def save_master_pwd(password):
    master_pwd = hash_sha256(password)
    settings.set_master_password(master_pwd)

def check_hash_sha265(value):
    return bool(re.match(__SHA265_REGEX, value))

def master_pwd_exists():
    master_pwd = settings.get_master_password()
    if master_pwd:
        return check_hash_sha265(master_pwd)
    return False

def master_pwd_valid(form_pwd):
    return settings.get_master_password() == hash_sha256(form_pwd)

def reset_all():
    services.entry_delete_all()
    services.category_delete_all()
    settings.init()