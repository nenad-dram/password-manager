"""
Module responsible for security operations like encryption, hashing and handling master password

Created on Jan 22, 2020
@author: nenad.dramicanin
"""

import hashlib
import re
from . import settings
from . import services
from cryptography.fernet import Fernet

# Constants
__SHA265_REGEX = '^[A-Fa-f0-9]{64}$'
__CRYPTO_KEY = '5S-kyu82tIgGEMET1GPKxCQrRC-xTBjTXMZkVn_PCoc='
__ENCODING_UTF8 = 'utf-8'


def hash_sha256(value: str) -> str:
    """Returns hash for provided value"""

    return hashlib.sha256(value.encode(__ENCODING_UTF8)).hexdigest()


def save_master_pwd(password: str):
    """Saves hashed value for master password provided as plain text"""

    master_pwd = hash_sha256(password)
    settings.set_master_password(master_pwd)


def check_hash_sha265(value: str) -> bool:
    """Checks whether provided value is valid hash string"""

    return bool(re.match(__SHA265_REGEX, value))


def master_pwd_exists() -> bool:
    """Checks whether valid master password exists"""

    master_pwd = settings.get_master_password()
    if master_pwd:
        return check_hash_sha265(master_pwd)
    return False


def master_pwd_valid(form_pwd: str) -> bool:
    """Checks whether provided value hash matches saved master password"""

    return settings.get_master_password() == hash_sha256(form_pwd)


def reset_all():
    """Returns application to initial state by deleting all existing data"""

    services.entry_delete_all()
    services.category_delete_all()
    settings.init()


def encrypt_data(source_text: str) -> str:
    """Encrypts provided source text using constant key"""

    cipher_suite = Fernet(__CRYPTO_KEY)
    cipher_text = cipher_suite.encrypt(source_text.encode())
    return cipher_text


def decrypt_data(cipher_text: str) -> str:
    """Decrypts provided cipher text using constant key"""

    cipher_suite = Fernet(__CRYPTO_KEY)
    source_text = cipher_suite.decrypt(cipher_text)
    return source_text.decode(__ENCODING_UTF8)
