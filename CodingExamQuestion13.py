"""Ask the user to enter a 3 digit number till he enters 0
              Print the square root of only 3 digit positive numbers.
              Make sure that the program does not print the square root of any number that is not a 3 digit number
"""
import math

while True:
    Number = int(raw_input("Enter a 3 digit number:"))
    if Number == 0 or Number == '':
        print "Entered Number is Zero or None"
        break
    elif len(str(Number)) == 3:
        print "Square Root of",Number,"is",math.sqrt(int(Number))


Output:

[suresh@localhost Python]$ python CodingExamQuestion13.py
Enter a 3 digit number:1
Enter a 3 digit number:2
Enter a 3 digit number:3
Enter a 3 digit number:4
Enter a 3 digit number:333
18.2482875909
Enter a 3 digit number:0
Entered Number is Zero or None
