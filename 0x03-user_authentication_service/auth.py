#!/usr/bin/env python3
'''
AUTH MODULE
'''
import bcrypt
import uuid
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> bytes:
    '''Hashing method for password'''
    password = password.encode('utf-8')
    hashed = bcrypt.hashpw(password, bcrypt.gensalt())
    return hashed


def _generate_uuid() -> str:
        '''Generate uuids'''
        gen_uuid = uuid.uuid4()
        return gen_uuid


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        '''Register new user.
        Use the methods from db class
        '''
        try:
            user = self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            pwd = _hash_password(password)
            newUser = self._db.add_user(email, pwd)
            return newUser

    def valid_login(self, email: str, password: str) -> bool:
        '''Validit password'''
        try:
            user = self._db.find_user_by(email=email)
            if bcrypt.checkpw(password.encode('utf-8'), user.hashed_password):
                return True
        except NoResultFound:
            return False
        else:
            return False

