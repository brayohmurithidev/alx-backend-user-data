#!/usr/bin/env python3
"""
Auth class module
"""
from typing import List, TypeVar
from flask import request


class Auth:
    '''Module that takes care of authentication'''
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Method that will be called before each request to validate if a
        request is authenticated or not
        """
        return False

    def authorization_header(self, request=None) -> str:
        """
        Method that handles authorization header to request.
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Method that retrieves the current user from request.
        """
        return None
