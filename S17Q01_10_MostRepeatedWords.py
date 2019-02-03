"""
S17Q01
Write a Python program that takes a file name as its argument.
This program should count the occurrences of all the words in a file.
   - It should then print the top 10 most repeated words
        in the descending order of their count.
   - Print a separate list of all the words that
        are not repeated in that file.
"""
import sys
from sys import argv
import re
fname = sys.argv[1]
dict1,cnt,Nonrepeated = {},0,{}
FH = open(fname,"r")
all_test = FH.read()
all_words = re.split(r'[. \n]', all_test)
set1 = set(all_words)
for i in set1:
   dict1[(i)]=int(all_words.count(i))
print "*"*70
print "Top 10 most repeated words"
for key, value in sorted(dict1.iteritems(), key=lambda (k,v): (v,k),reverse=True):
    if cnt < 10 and key != "":
        print "%s: %s" % (key, value)
        cnt += 1
print "Words that are not repeated"
print "*"*70
for key, value in sorted(dict1.iteritems(), key=lambda (k,v): (v,k),reverse=True):
    if value == 1:
        Nonrepeated[(key)] = value
print Nonrepeated.keys()
"""
for w in all_words:
    if w.strip() != "":
"""
