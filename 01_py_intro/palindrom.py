"""
# UE 1 - 24.09.26 F
"""

import re

__author__ = "Clemens Zimmer"
__example__ = "SEW4/01/F"
__date__ = "24.09.2026"
__license__ = "GNU GPLv3"


def is_palindrom(s: str):
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


def is_palindrom_sentence(s: str):
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
    TypeError: expected string or bytes-like object, got 'float'

    """

    s = re.sub(r"[\s\W_]+", "", s).lower()
    return s == s[::-1]


def palindrom_product(x) -> int:
    """
    >>> palindrom_product(1000000)
    906609
    >>> palindrom_product(906609)
    888888
    >>> palindrom_product(100000)
    99999
    >>> palindrom_product(100)
    -1
    >>> palindrom_product(0)
    -1

    """

    max_value = -1
    for i in range(100, 1000):
        for e in range(100, 1000):
            current = i * e
            if current >= x:
                break
            if is_palindrom(str(current)):
                if current > max_value:
                    max_value = current
    return max_value


def get_dec_hex_palindrom(x):
    """
    >>> get_dec_hex_palindrom(1000)
    979
    >>> get_dec_hex_palindrom(900)
    787
    >>> get_dec_hex_palindrom(700)
    626
    """
    set_saved = set()
    i, e = 0, 0
    max_value = -1
    while i <= x:
        i+=1
        while e <= x:
            e+=1
            current = i * e
            if set_saved.__contains__(current):
                continue
            set_saved.add(current)
            if current >= x:
                break
            if is_palindrom(str(current)) and is_palindrom(str(hex(current))[2:]):
                if current > max_value:
                    max_value = current
        e = 0
    return max_value


def to_base(number:int, base:int)->str:
    """
    :param number: Zahl im 10er-Syste,
    :param base: Zielsystem (maximal 36)
    :return: Zahl im Zielsystem als String
    >>> to_base(1234,16)
    '4D2'
    >>> to_base(10, 2)
    '1010'
    >>> to_base(255, 16)
    'FF'
    >>> to_base(35, 36)
    'Z'
    >>> to_base(1234, 16)
    '4D2'
    >>> to_base(123456, 16)
    '1E240'
    >>> to_base(1000000, 2)
    '11110100001001000000'
    >>> to_base(987654321, 36)
    'GC0UY9'
    """
    all_chars = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
     'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
     'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
     'U', 'V', 'W', 'X', 'Y', 'Z')
    if  2 < base > 36:
        raise ValueError('base must be between 2 and 36')
    n = number
    str_out = ""
    while n != 0:
        str_out += all_chars[n%base]
        n = n // base

    return str_out[::-1]

def main():
    pass


if __name__ == "__main__":
    main()
