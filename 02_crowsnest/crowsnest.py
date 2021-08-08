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
    parser.add_argument('-s',
                        '--side',
                        help='The side of the ship',
                        metavar='side',
                        type=str,
                        default='larboard')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """All logic"""

    args = get_args()
    danger = args.danger
    side = args.side

    starting_char = danger[0]
    preposition = 'an' if starting_char.lower() in 'aeiou' else 'a'
    preposition = preposition.capitalize() if starting_char.isupper() else preposition

    print(f'Ahoy, Captain, {preposition} {danger} off the {side} bow!')


# --------------------------------------------------
if __name__ == '__main__':
    main()
