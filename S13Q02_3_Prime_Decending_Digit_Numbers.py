"""
Create a text file num.txt that contains one number per line.
These numbers can be 1, 2, 3 or 4 digit numbers.
- Write a program to read the numbers from this file
- Discard all numbers that are not 3 digit numbers.
- From all the 3 digit numbers in the file,
    find and print the prime numbers in descending order.
"""
from S13Q01_3_digit_Number import primecheck 
FH = open("num.txt","r")
all_text = FH.read()
all_lines = all_text.split()
numbers,a= [],[]
for i in all_lines:
    if len((i)) == 3:
        a = primecheck(int(i))
        if a != None:
            numbers.append(int(a))
            numbers.sort(reverse=True)
print numbers    
FH.close()
