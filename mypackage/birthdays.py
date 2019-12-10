"""

This is our birthday module

"""

'''Open the birth.csv which contains 

'''

import csv

reader = csv.reader (open('mypackage/birth.csv', 'r'))
d = {}
for row in reader:
    k,v = row  
    d[k]= v

"""Functions

"""

def print_birthdays():
    """Return famous people's names of the csv"""
    print('We know the birthdays of these people:')
    for e in d:
        print(e)

def return_birthday(name):
    """Given a name, if found, return the birthdays"""
    if name in d:
        return d[name]
    else:
        return False 

