'''
Created on Jan 22, 2020

@author: ndramica
'''
import hashlib
import re
from model import settings, services
from cryptography.fernet import Fernet

__SHA265_REGEX = '^[A-Fa-f0-9]{64}$'
__CRYPTO_KEY = '5S-kyu82tIgGEMET1GPKxCQrRC-xTBjTXMZkVn_PCoc='
__ENCODING_UTF8 = 'utf-8'


def hash_sha256(value):
    return hashlib.sha256(value.encode(__ENCODING_UTF8)).hexdigest()


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


def encrypt_data(source_text):
    cipher_suite = Fernet(__CRYPTO_KEY)
    cipher_text = cipher_suite.encrypt(source_text.encode())
    return cipher_text


def decrypt_data(cipher_text):
    cipher_suite = Fernet(__CRYPTO_KEY)
    source_text = cipher_suite.decrypt(cipher_text)
    return source_text.decode(__ENCODING_UTF8)
