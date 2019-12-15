"""This is our birthday module."""

import csv

"""Open the birth.csv."""

reader = csv.reader(open('mypackage/birth.csv', 'r'))
d = {}
for row in reader:
    k, v = row
    d[k] = v

"""These are the functions."""


def print_birthdays():
    """Return famous people's names of the csv."""
    print('We know the birthdays of these people:')
    for e in d:
        print(e)


def return_birthday(name):
    """Given a name, if found, return the birthdays."""
    if name in d:
        return d[name]
    else:
        return False
