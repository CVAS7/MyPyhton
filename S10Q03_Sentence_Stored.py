"""
S10Q03
Write a Python script that takes a file name as its argument.
Write the contents of this file to another file such that,
   each sentence is stored on a new line.

"""
# You have three options for punctuating the end of a sentence: a period(.) an exclamation mark(!) or a question mark(?)
import re
import sys
from sys import argv
fname = sys.argv[1]
FH = open(fname,"r")
x = FH.read()
a = re.split(r'[.!?]', x)
WFH = open("New"+fname,"w+")
for i in a:
    print i,type(i)
    WFH.write(i)
print "Your new file name is","New"+fname
FH.close()
WFH.close()
