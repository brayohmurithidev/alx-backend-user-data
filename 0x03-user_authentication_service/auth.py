#!/usr/bin/env python3
'''
AUTH MODULE
'''
import bcrypt
import uuid
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
from typing import Union


def _hash_password(password: str) -> bytes:
    '''Hashing method for password'''
    password = password.encode('utf-8')
    hashed = bcrypt.hashpw(password, bcrypt.gensalt())
    return hashed


def _generate_uuid() -> str:
    '''Generate uuids'''
    gen_uuid = uuid.uuid4()
    return str(gen_uuid)


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

    def create_session(self, email: str) -> str:
        '''Method to create a session id'''
        try:
            user = self._db.find_user_by(email=email)
            sess_id = _generate_uuid()
            self._db.update_user(user.id, session_id=sess_id)
            return str(user.session_id)
        except NoResultFound:
            return None

    def get_user_from_session_id(self, session_id: str) -> User or None:
        '''Get User from session'''
        # print(session_id)
        if session_id is None:
            return None
        try:
            user = self._db.find_user_by(session_id=session_id)
            return user
        except NoResultFound:
            return None

    def destroy_session(self, user_id: int) -> None:
        '''Destroy a session'''
        self._db.update_user(user_id, session_id=None)
        return None

    def get_reset_password_token(self, email: str) -> str:
        '''GET RESET PASSWORD TOKEN'''
        try:
            user = self._db.find_user_by(email=email)
            uuid = _generate_uuid()
            self._db.update_user(user.id, reset_token=uuid)
            return user.reset_token
        except NoResultFound:
            raise ValueError
        
    def update_password(self, reset_token: str, password: str) -> None:
        '''Update password to new password'''
        try:
            user = self._db.find_user_by(reset_token=reset_token)
            hashed = _hash_password(password)
            self._db.update_user(user.id, hashed_password=hashed, reset_token=None)
            return None
        except NoResultFound:
            return ValueError  