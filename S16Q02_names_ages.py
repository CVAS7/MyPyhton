"""
S16Q02
Write a Python program that prompts the user for a file. 
This file contains names of people and their ages. 
Read the file, and print the list with the oldest persons name listed first. 
A sample file [ AGES.TXT ] is shown above :
"""
"""
AGES.TXT
Dinesh - 22
Victor - 38
Sandeep - 58
Henry - 47
Akash - 18
Vishal - 29
Manish - 62
Ben - 32
"""
dict1 = {}
fname = raw_input("Enter the input file name:")
FH = open(fname,"r")
for l in FH:
    (k,v)=l.split("-")
    dict1[(k)] = int(v)
for key, value in sorted(dict1.iteritems(), key=lambda (k,v): (v,k),reverse=True):
    print "%s: %s" % (key, value)  
