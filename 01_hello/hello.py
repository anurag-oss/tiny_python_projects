#! /usr/bin/env python3
"""
Author: anurag-oss
Purpose: Say hello
"""

import argparse


def get_args():
    """Get the command line arguments"""
    parser = argparse.ArgumentParser(description='Say hello')
    parser.add_argument('-n', '--name', metavar='name',
                        default='World', help='Name to greet')
    return parser.parse_args()


def main():
    """Added the havy lifting program logic"""
    args = get_args()
    print('Hello, ' + args.name + '!')


if __name__ == '__main__':
    main()
