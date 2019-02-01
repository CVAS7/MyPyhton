"""
Write a Python program that takes a file name as its argument.
This file contains names of people and their corresponding contact numbers.
Read the file, and print the list in the ascending order of their names.
A sample file [ CONTACT_LIST.TXT ] is shown below :
Sumeet : 82736
David : 55283
Viney : 22783
James : 19923
Santosh :77283
Victor : 92384
Amit: 66271
Harry :38273 
"""
import sys
from sys import argv
fname = argv[1]
mydict = {}
FH = open(argv[1],"r")
print "Text Input file\n"
print FH.read(),
FH.seek(0)
print "Ascending order of their names\n"
for line in FH:
    (key,val) = line.split(":")
    mydict[(key)] = val
keys = mydict.keys()
keys.sort()
for i in keys:
    print "%s: %s" % (i, mydict[i]),
