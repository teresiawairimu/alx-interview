#!/usr/bin/env python3
""""Determine if a data set represents a valid UTF-8 encoding"""


def validUTF8(data):
    """Function determines if a data set represents
    UTF-8 encoding

    Parameter:
        data: the data set to be evaluated
    Returns:
        True if data set is valid UTF-8 encoding
        or False if it is invalid
    """
    number_of_bytes = 0
    mask1 = 1 << 7
    mask2 = 1 << 6  
    for num in data:
        byte = num & 0xFF
        if number_of_bytes == 0:
            if (byte & mask1) == 0:
                continue
            elif (byte & (mask1 >> 1)) == mask1:
                number_of_bytes = 1
            elif (byte & (mask1 >> 2)) == (mask1 >> 1):
                number_of_bytes = 2
            elif (byte & (mask1 >> 3)) == (mask1 >> 2):
                number_of_bytes = 3
            else:
                return False
        else:
            if not (byte & mask1 and not (byte & mask2)):
                return False
            number_of_bytes -= 1
    return number_of_bytes == 0
