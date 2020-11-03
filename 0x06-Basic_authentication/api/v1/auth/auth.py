#!/usr/bin/env python3
""" Auth module
"""
from flask import request
from typing import List, TypeVar


class Auth():
    """
    Auth class
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        require_auth function
        """
        if path is not None:
            if path[len(path) - 1] is not '/':
                path += '/'
        if path is None or path not in excluded_paths:
            return True
        if excluded_paths is None or excluded_paths == '':
            return True
        return False

    def authorization_header(self, request=None) -> str:
        """
        authorization_header function
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        current_user function
        """
        return None
