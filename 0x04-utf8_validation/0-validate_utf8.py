#!/usr/bin/env python3
""""Determine is a data represents a valid UTF-8 encoding"""


def validUTF8(data):
    """Function determines if a data set represents
    UTF-8 encoding

    Parameter:
        data: the data set to be evaluated
    Returns:
        True if data set is valid UTF-8 encoding
        or False if it is invalid
    """
    num_bytes = 0

    mask1 = 1 << 7  # 10000000
    mask2 = 1 << 6  # 01000000

    for num in data:
        byte = num & 0xFF

        if num_bytes == 0:
            if (byte & mask1) == 0:
                continue
            elif (byte & (mask1 >> 1)) == mask1:
                num_bytes = 1  # 2-byte character (110xxxxx)
            elif (byte & (mask1 >> 2)) == (mask1 >> 1):
                num_bytes = 2  # 3-byte character (1110xxxx)
            elif (byte & (mask1 >> 3)) == (mask1 >> 2):
                num_bytes = 3  # 4-byte character (11110xxx)
            else:
                return False
        else:
            if not (byte & mask1 and not (byte & mask2)):
                return False
            num_bytes -= 1
    return num_bytes == 0

