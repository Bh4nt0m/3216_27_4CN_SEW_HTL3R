"""

"""

import re

__author__ = "Clemens Zimmer"
__example__ = "SEW4/01/F"
__date__ = "24.09.2026"
__license__ = "GNU GPLv3"

def is_palindrom(s:str):
    """
    >>> is_palindrom("anna")
    True

    >>> is_palindrom("anno")
    False

    >>> is_palindrom("")
    True

    >>> is_palindrom(3.14)
    Traceback (most recent call last):
     ...
    TypeError: 'float' object is not subscriptable

    """
    return s == s[::-1]

def is_palindrom_sentence(s:str):
    """
    >>> is_palindrom_sentence("Was it a car or a cat I saw")
    True

    >>> is_palindrom_sentence("1 23.456789,87654?321")
    True

    >>> is_palindrom_sentence("xsdertzhnm")
    False

    >>> is_palindrom_sentence("")
    True

    >>> is_palindrom_sentence(3.14)
    Traceback (most recent call last):
     ...
    AttributeError: 'float' object has no attribute 'lower'

    """

    s = s.lower().replace(" ", "").replace(".", "").replace(",", "").replace("-", "").replace("!", "").replace("?", "")
    return s == s[::-1]


def main():
    pass

if __name__ == "__main__":
    main()




