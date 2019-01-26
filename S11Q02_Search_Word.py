"""
S11Q02
Write a Python program that takes a file as the first argument 
   and a search word as the second argument. 
This script should print only those lines that have the search word
"""
import sys
from sys import argv
fname = sys.argv[1]
word = sys.argv[2]
FH = open("Newdemofile7.txt","r")
all_text = FH.read()
all_lines = all_text.split("\n")
cnt = 1
for i in all_lines:
    cnt += 1
    results = i.find(word)
    if results != -1:
        print "Line numeber contains",word,"is",cnt,"And line content is",i
#for i in FH.readline():
#    print i
FH.close()
