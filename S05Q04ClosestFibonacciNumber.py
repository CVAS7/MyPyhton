#!/usr/bin/python
"""- Check if a given number is a fibonacci number. 
           If not, then print the closest fibonacci number to the given number"""

n1 = 1
n2 = 1
fib = [n1,n2]
number = input("Enter the number:")
i = 0
while (i <= number):
    i += 1
    n3 = n1+n2
    n1 = n2
    n2 = n3
    fib.append(n3)
if number in fib:
    print ("Given number is fibonacci")
else:
    print "Given number is not fibonacci"
