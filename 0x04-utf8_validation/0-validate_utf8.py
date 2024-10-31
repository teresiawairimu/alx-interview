#!/usr/bin/env python3
"""Determines if a data set represents a valid UTF-8 encoding"""


def validUTF8(data):
    """Determines whether a data set represents a valid UTF-8 encoding
    Returns:
        True if a valid UTF-8
        or False if invalid
    """
    number_of_bytes = 0

    for byte in data:
        byte = byte & 0xFF
        if number_of_bytes == 0:
            if (byte >> 7) == 0b0:
                continue
            elif (byte >> 5) == 0b110:
                number_of_bytes = 1
            elif (byte >> 4) == 0b1110:
                number_of_bytes = 2
            elif (byte >> 3) == 0b11110:
                number_of_bytes = 3
            else:
                return False
        else:
            if (byte >> 6) != 0b10:
                return False
            number_of_bytes -= 1
    return number_of_bytes == 0
