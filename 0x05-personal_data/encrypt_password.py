#!/usr/bin/env python3
"""
encrypt_password
"""
import bcrypt


def hash_password(password: str):
    """
    hash_password function
    """
    password = bytes(password, 'utf-8')
    return bcrypt.hashpw(password, bcrypt.gensalt())
