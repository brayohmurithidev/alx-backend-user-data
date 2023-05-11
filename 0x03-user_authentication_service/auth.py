#!/usr/bin/env python3
'''
AUTH MODULE
'''
import bcrypt
import base64


def _hash_password(password: str) -> bytes:
    '''Hashing method for password'''
    password = password.encode('utf-8')
    hashed = bcrypt.hashpw(password, bcrypt.gensalt())
    return hashed
