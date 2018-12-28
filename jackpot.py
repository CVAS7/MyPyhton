from sys import argv
import sumops
from random import randint
"""
if num1 == None:
    print "enter a 5 digit number"
    num1 = raw_input()
    num1 = int(num1)
    a = sumops.dsum(num1)
    print a
    b = (random.randint(1,50))
    print b
    if (b == a):
        print "You won the jackpot"
    else:
        print "the random number",b
"""
def fivedigit ():
    if len(argv) == 1:
        num1 = int(raw_input("Enter a 5 digit number"))
        return num1 
    else:
        num1 = argv[1]
        return num1
        
#Main here
c = fivedigit()
e = sumops.dsum(c)
print "Sum of Digits for given number",e
d = (randint(1,50))
if (d == e):
    print "You won the jackpot"
else:
    print "The random number",d

================================================
================================================
================================================
Output:
python sumops.py 1111
Sum of Digits in 1111 is 4
python sumops.py 11111
Sum of Digits in 11111 is 5
python jackpot.py 1111111111
Sum of Digits for given number 10
The random number 4
python jackpot.py 1111111111
Sum of Digits for given number 10
The random number 46
