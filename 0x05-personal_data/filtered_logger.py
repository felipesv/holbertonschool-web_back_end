#!/usr/bin/env python3
"""
Regex-ing
"""
from re import sub
from typing import List
import logging


class RedactingFormatter(logging.Formatter):
    """
    Redacting Formatter class
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """
        Constructor
        """
        self.fields = fields
        super(RedactingFormatter, self).__init__(self.FORMAT)

    def format(self, record: logging.LogRecord) -> str:
        """
        format function
        """
        return filter_datum(self.fields, self.REDACTION,
                            super().format(record), self.SEPARATOR)


def get_logger() -> logging.getLogger:
    """
    get_logger function
    """
    logging.(filename='user_data', level=logging.INFO)


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """
    filter_datum function
    """
    for field in fields:
        # . -> match a character
        # + -> match more than one
        # ? -> repeat the next text of the match
        message = sub(fr'{field}=.+?{separator}',
                      f'{field}={redaction}{separator}', message)
    return message
