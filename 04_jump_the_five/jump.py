#!/usr/bin/env python3
"""
Author : anumishr <anumishr@localhost>
Date   : 2021-08-08
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Jump the Five',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='str',
                        type=str,
                        help='The text to encode')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    text_to_encode = args.text

    jumper_lookup = {
        '1': '9',
        '2': '8',
        '3': '7',
        '4': '6',
        '5': '0',
        '6': '4',
        '7': '3',
        '8': '2',
        '9': '1',
        '0': '5'
    }

    output_list = [jumper_lookup.get(c, c) for c in text_to_encode]

    encoded_text = ''.join(output_list)

    print(encoded_text)


# --------------------------------------------------
if __name__ == '__main__':
    main()
