# api/v1/auth/auth.py
"""
Authentication module for the API.
"""

from typing import List, TypeVar
from flask import request


class Auth:
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Public method to check if authentication is required.
        Currently always returns False.
        """
        return False

    def authorization_header(self, request=None) -> str:
        """
        Public method to get the value of the Authorization header.
        Currently always returns None.
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Public method to get the current user.
        Currently always returns None.
        """
        return None
