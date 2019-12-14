"""This is our main file."""

# ! /usr/bin/env python3
import sys
import argparse

# from birthdays import return_birthday
from mypackage import birthdays

"""Given one or more name return the birth date
   with different level of verbosity
   if they are in the csv.
"""

parser = argparse.ArgumentParser(
    prog="This program returns the birthdays of famous people")
parser.add_argument('n', nargs='+',
                    help='Insert one or more name with format: "Name Surname"')
parser.add_argument('-v', '--verbosity', action='count', default=0,
                    help='Decide the level of verbosity')
args = parser.parse_args()


"""Different output for different levels of verbosity."""

# verbosity option
name = args.n

for i in name:
    # if args.verbosity:
    if birthdays.return_birthday(i):
        if args.verbosity >= 2:
            print('{} was born the {}'.format(i, birthdays.return_birthday(i)))
        elif args.verbosity >= 1:
            print('{} : {}'.format(i, birthdays.return_birthday(i)))
        else:
            print(birthdays.return_birthday(i))
    else:
        print('Sorry, {} is not in the list, '.format(i))
        birthdays.print_birthdays()
