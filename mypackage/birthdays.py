"""

This is our birthday module

"""

'''
open the birth.csv which contains 
'''

import csv

reader = csv.reader (open('birth.csv', 'r'))
d = {}
for row in reader:
    k,v = row  
    d[k]= v

"""
functions
"""
def print_birthdays():
    """Return famous people's names of the csv"""
    print('Welcome to the birthday dictionary. We know the birthdays of these people:')
    for e in d:
        print(e)

def return_birthday(name):
    """Given a name, if found, return the birthdays"""
    if name in d:
        print('{}\'s birthday is {}.'.format(name, d[name]))
    else:
        print('Sadly, we don\'t have {}\'s birthday.'.format(name))

