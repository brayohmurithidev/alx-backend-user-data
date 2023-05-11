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


from db import DB
from user import User


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        '''Register new user. 
        Use the methods from db class
        '''
        user = self._db._session.query(User).filter(User.email == email).first()
        if user is not None:
            raise ValueError(f"User {email} already exists")
        pwd = _hash_password(password)
        newUser = self._db.add_user(email, pwd)
        return newUser