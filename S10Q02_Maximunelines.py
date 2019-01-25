"""
S10Q02
Write a Python script that takes a file name as its argument.
In that file, find the line that has the maximum number of
occurrences of the letter e
"""
import sys
from sys import argv
fname = sys.argv[1]
FH = open(fname,"r")
a = FH.readlines()
count,total = 0,[]
#print a
FH.seek(0)
for i in xrange(len(a)):
    b = FH.readline()
    for c in b:
        if c == "e":
            count += 1
    total.append((count))
#    print count
#    print "-"*100
    count = 0
print "="*100
print "This line number",total.index(max(total))+1,"havig maximun number of letter e"
print "="*100
FH.close()
