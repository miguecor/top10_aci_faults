#!/usr/local/bin/python3
"""
This is a short function definition that will provide timestamp
in the form of a string with the format: 'yyyymmdd_hhmmss'.
"""

import time


def timestamp():
    now = time.localtime()
    try:
        stamp = str(f'{now.tm_year}.{now.tm_mon}.{now.tm_mday}'
                        f'_{now.tm_hour}.{now.tm_min}.{now.tm_sec}')

    except Exception as val:
        print("Something went wrong!")
        print("Error: ", val)

    return stamp

