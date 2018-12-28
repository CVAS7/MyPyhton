"""
Create a log table of base 10 for all numbers from 1 to 10.
Then create a log table to base 10 for all numbers from 1 to 100
that are multiples of 10.
Make sure the log values are printed unto 4 decimal places.
Display the log tables as shown below.
What similarities and differences do you see in the 2 tables ?
"""
from math import log

def logtable10(a,b):
    x = log(i,b)
    if len(str(i))==1:
        print i,"  ___" ,round(x,4)
    elif len(str(i))==2:
        print i," ___" ,round(x,4)
    else:
        print i,"___" ,round(x,4)


#Main here
print "Table I"
for i in xrange(1,11):
    logtable10(i,10)


print "Table II"    
for i in xrange(1,101):
    if (i%10) == 0:
        logtable10(i,10)

print ("Similarities:Decimal Values are same \nDifferences:Whole Number are incremented by 1")
===================================
===================================
===================================
Output:
Table I
1   ___ 0.0
2   ___ 0.301
3   ___ 0.4771
4   ___ 0.6021
5   ___ 0.699
6   ___ 0.7782
7   ___ 0.8451
8   ___ 0.9031
9   ___ 0.9542
10  ___ 1.0
Table II
10  ___ 1.0
20  ___ 1.301
30  ___ 1.4771
40  ___ 1.6021
50  ___ 1.699
60  ___ 1.7782
70  ___ 1.8451
80  ___ 1.9031
90  ___ 1.9542
100 ___ 2.0
================================================
================================================
================================================
Similarities:Decimal Values are same 
Differences:Whole Number are incremented by 1
