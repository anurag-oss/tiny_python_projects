#!/usr/bin/env python3
"""
Author : anumishr <anumishr@localhost>
Date   : 2021-08-10
Purpose: Rock the Casbah
"""

import argparse
import os


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Howl back!!!',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text_or_file',
                        metavar='str',
                        type=str,
                        help='A file name or text')

    parser.add_argument('-o',
                        '--outfile',
                        help='An optional output file to write',
                        metavar='str',
                        type=str,
                        default='')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    text_or_file = args.text_or_file
    outfile = args.outfile
    is_file_exists = True if os.path.isfile(text_or_file) else False

    if is_file_exists:
        text_or_file = read_file(text_or_file)

    text_or_file = text_or_file.upper()

    if outfile != '':
        write_file(outfile, text_or_file)
    else:
        print(text_or_file)


def read_file(file_name):
    with open(file_name, mode='rt') as file_handle:
        file_as_str = file_handle.read()
        return file_as_str


def write_file(file_name, content):
    with open(file_name, mode='wt') as file_handle:
        file_handle.write(content)


# --------------------------------------------------
if __name__ == '__main__':
    main()
