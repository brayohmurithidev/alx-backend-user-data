#!/usr/bin/env python3
""" Module for API authentication """
from flask import request
from typing import List, TypeVar


class Auth:
    """ Class to manage API authentication """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Method to validate if endpoint requires authentication """
        if not path or not excluded_paths or excluded_paths == []:
            return True

        if path.endswith("/"):
            path = path[:-1]

        for excluded_path in excluded_paths:
            if excluded_path.endswith("*"):
                if path.startswith(excluded_path[:-1]):
                    return False
            elif excluded_path == path:
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """ Method to handle authorization header """
        if request is None:
            return None

        return request.headers.get("Authorization", None)

    def current_user(self, request=None) -> TypeVar('User'):
        """ Method to validate the current user """
        return None
