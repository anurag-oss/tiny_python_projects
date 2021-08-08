#!/usr/bin/env python3
"""
Author : anumishr <anumishr@localhost>
Date   : 2021-08-07
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Food items to bring to the picnic',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('food_items', 
                        nargs='+', 
                        type=str,
                        metavar='str', 
                        help='Food Items')

    parser.add_argument('-s',
                        '--sorted',
                        help='A boolean flag to sort',
                        action='store_true')

    parser.add_argument('-i',
                        '--ignore-comma',
                        dest='ignore_comma',
                        help='A boolean flag to supress oxford comma',
                        action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    food_items = args.food_items
    should_sort = args.sorted
    ignore_comma = args.ignore_comma
    
    if should_sort:
        food_items.sort()

    formatted_food_items = format_list_of_food(food_items, ignore_comma)

    print(f'You are bringing {formatted_food_items}.')


def format_list_of_food(food_items, ignore_comma):
    formatted_food_items = ', '.join(food_items)
    last_separator = ', and' if len(food_items) >= 3 and not ignore_comma else ' and'
    last_comma_index = formatted_food_items.rfind(",")
    if last_comma_index == -1:
        return formatted_food_items

    formatted_food_items_last_and = formatted_food_items[:last_comma_index] + \
        last_separator + \
        formatted_food_items[last_comma_index + 1:]

    return formatted_food_items_last_and


# --------------------------------------------------
if __name__ == '__main__':
    main()
