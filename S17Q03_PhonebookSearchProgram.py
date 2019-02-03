"""
S17Q03 - Phonebook Search Program
Write a Python program that takes a file name as its argument.
This file contains names of people and their corresponding contact numbers.
- Prompt the user to enter a few characters to search for.
- Print all the names that contain this sequence of characters
     in the ascending order of their names
"""
import sys
from sys import argv
dict1 = {}
skey = raw_input("Enter text you wnat to search:")
lskey = skey.lower()
FH = open(sys.argv[1],"r")
for l in FH:
    value1 = l.strip().split(",")
    dict1[str(value1[0])] = value1[8]
    if (str(value1[0]).lower()).find(lskey) != -1:
        print str(value1[0]),"=>",value1[8]
