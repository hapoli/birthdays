"""This is our main file."""

# ! /usr/bin/env python3
import sys
import argparse
from birth_package import birthdays

"""Given one or more name return the birth date
   with different level of verbosity
   if they are in the csv.
"""

def parse_argument():
    """Insert the famous people's name and your credentials."""
    parser = argparse.ArgumentParser(
             prog="This program return the birthday of famous people")

    parser.add_argument('n', nargs='+',
             help="You can insert one or names in the format: 'Name Surname'")
 
    parser.add_argument('-v', '--verbosity', action='count', default=0,
              help="Decide the level of verbosity")

    #Check for username and password
    parser.add_argument('-p', help="the username password",
                        required=True)
    parser.add_argument('-c', help="check for a usernamename and password"
                       "(requires -p)", required=True)
    args = parser.parse_args()
    return args

def verbosity_levels(name):
    """the different verbosity levels"""
    for i in name:
    #if args.verbosity:
        if birthdays.return_birthday(i):
            if args.verbosity >= 2:
                print('{} was born the {}'.format(i, 
                       birthdays.return_birthday(i)))
            elif args.verbosity >= 1:
                print ('{} : {}'.format(i, birthdays.return_birthday(i)))
            else:
                print (birthdays.return_birthday(i))
        else:
            print ('Sorry, {} is not in the list, '.format(i))
            birthdays.print_birthdays()

db_corr = 'user_database.db'

if __name__ == "__main__":
     parse_argument()   
     args = parse_argument()
     if dbmanager.check_for_username(args.c, args.p, db_corr):
         verbosity_levels(args.n)




