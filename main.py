#! /usr/bin/env python3

from mypackage import return_birthday, birthdays
import sys
import argparse

'''Given one or more name return the birth date with different level of 
verbosity if they are contained in the csv

'''

parser = argparse.ArgumentParser(
         prog="This program returns the birthdays of famous people")
parser.add_argument('n', nargs='+', 
         help='Insert one or more name in the format: "Name Surname"')  
parser.add_argument('-v', '--verbosity', action = 'count', default= 0,
         help='Decide the level of verbosity')
args = parser.parse_arg()


if len(sys.argv)>1:
    birthdays.return_birthday(sys.argv[1])
else:
    print("You didn't pass any argument")
