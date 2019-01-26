[suresh@localhost Python]$ cat S11Q01_Number_Max_Sum.py
"""S11Q01
From a file that contains a list of numbers.
Find the maximum number in that list. 
Also find the sum of all the numbers in that list.
"""
import sys
from sys import argv
filepath = argv[1]
sum1 = 0
with open(filepath) as FH:
    a = (FH.readlines())
#    print a,type(a),max(a)
    print "-"*100
    b = [int(i.split('\n', 1)[0]) for i in a]
    print "Maximun number in the number file:",max(b)
    print "-"*100
for i in b:
    sum1 = sum1+i
print "Sum of the number in file:",sum1
print "-"*100

