#!/usr/bin/env python3
"""
Regex-ing
"""
import re
from typing import List


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """
    filter_datum function
        # . -> match a character
        # + -> match more than one
        # ? -> repeat the next text of the match
    """
    for field in fields:
        message = re.sub(fr'{field}=.+?{separator}',
                      f'{field}={redaction}{separator}', message)
    return message
