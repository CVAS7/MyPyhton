#!/usr/bin/python
""" - Take a number as input from the user. 
           Print all the squares of numbers from 1 to any large number. 
           The numbers printed should be less than 
                 the number given as input by the user"""
number = input("Enter the number:")
i = 0
while (i <= number):
    i += 1
    sqr = i*i
    if sqr <= number:
        print i*i
