#!/usr/bin/python
"""  - Ask the user to enter a number till he enters 0. 
          Print the maximum and minimum values among all entered numbers. 
          Print the number of single, two and three digit numbers entered."""
number = input("Enter the number:")
i = 0
numbers = [number]
while (number != 0):
    i += 1
    number = input("Enter the number:")
    numbers.append (number)

print numbers

single,two,three,otherdigits = 0,0,0,0
for val in numbers:
    if (0 < val < 10):
        single = single+1

    elif (10 <= val < 100 ):
        two = two+1

    elif (100 <= val < 1000):
        three = three+1

    else:
        otherdigits = otherdigits+1
print "Count of Single Digits    ",single
print "Count of Two Digits       ",two
print "Count of Three Digits     ",three
print "Count of Other1,2,3 Digits",otherdigits-1
