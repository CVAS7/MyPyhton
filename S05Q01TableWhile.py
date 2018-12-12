#!/usr/bin/python
"""Print the multiplication table of a given number using for and while loops"""
number = input("Which Numbers Multiplication Table do you neeed to print:")
till = input("Till what number you want to print:")
print "Multplication Table of",number,"....."
i = 0
while (i != till): 
    i += 1
    print number,"*",i,"=",number*i 
