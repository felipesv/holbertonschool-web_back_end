#!/usr/bin/env python3
""" Auth module
"""
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """
    Basic Auth class
    """

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """
        extract_base64_authorization_header function
        """
        if authorization_header is None:
            return None
        if type(authorization_header) is not str:
            return None
        if authorization_header[0:6] != 'Basic ':
            return None
        return authorization_header[6:]
