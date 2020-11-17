#!/usr/bin/env python3
"""
Module auth
"""
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> str:
    """
        Hash a password
        Return the encrypted  password
    """
    return bcrypt.hashpw(bytes(password, 'utf-8'), bcrypt.gensalt())


class Auth:
    """
        Auth class
        create model to manage the Authentication
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """
            Register a user with email and pass
            Return the User registered
        """
        try:
            user = self._db.find_user_by(email=email)
            if user:
                raise ValueError("User {} already exists".format(email))
        except NoResultFound:
            pass
        password = _hash_password(password)
        user = self._db.add_user(email=email, hashed_password=password)
        return user
