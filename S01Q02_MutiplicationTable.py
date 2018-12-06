#!/usr/bin/python
tabNum = input("Which Table you what to print: ")
print "Multiplication Table of Number ", tabNum

def MulTable(n1,n2):
    line = n1*n2
    print n1, " * ", n2, " = ", line


#Main
f = range(1,20)
for x in f:
    value = MulTable(x,tabNum)
