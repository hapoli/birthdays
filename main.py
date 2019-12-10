#! /usr/bin/env python3

from mypackage import birthdays
import sys

"""Given the user's input apply return_birthday. """

if len(sys.argv)>1:
    birthdays.return_birthday(sys.argv[1])
else:
    print("You didn't pass any argument")
