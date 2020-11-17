#!/usr/bin/env python3
"""
Module auth
"""
import bcrypt


def _hash_password(password: str) -> str:
    """
        Hash a password
        Return the encrypted  password
    """
    return bcrypt.hashpw(bytes(password, 'utf-8'), bcrypt.gensalt())
