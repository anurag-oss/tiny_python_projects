#!/usr/bin/env python3
"""
Author : 12304856+anurag-oss@users.noreply.github.com
Date   : 2021-08-07
Purpose: Warn the captain of imminent danger
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Warn the captain of imminent danger',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('danger', metavar='danger', help='The imminent danger')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """All logic"""

    args = get_args()
    danger: str = args.danger

    starting_char = danger[0].lower()
    preposition = ""

    if starting_char in ("a", "e", "i", "o", "u"):
        preposition = "an"
    else:
        preposition = "a"

    print(f'Ahoy, Captain, {preposition} {danger} off the larboard bow!')


# --------------------------------------------------
if __name__ == '__main__':
    main()
