#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from typing import Dict, Union, Any

from user import Base, User


class DB:
    """DB class
    """
    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """Method to add a user
        """
        user = User(email=email, hashed_password=hashed_password)
        session = self._session
        session.add(user)
        session.commit()
        user_obj = session.query(User).filter(User.id == user.id).first()
        return user_obj

    def find_user_by(self, **kwargs: Dict[str, Any]) -> User:
        '''Find user and filter by arbitrary arguments.
        '''
        # Initialize the query obj
        query = self._session.query(User)
        for key, value in kwargs.items():
            try:
                # Try filter and if an attribute error throw invalid err.
                query = query.filter(getattr(User, key) == value)
            except AttributeError:
                raise InvalidRequestError
            # Check if user exists.
        if query.first() is None:
            raise NoResultFound
        return query.first()
