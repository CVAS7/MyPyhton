#!/usr/bin/python
"""
To find input number is Luncky Number or not
"""
L = 17
n = input ("Enter your Guess Number to check:\nWhich is in the Range of 1 to 25 \nif it is Luncky Number or Not ")

def almost():
    if (L == n):
        print ("------------------------------------")
        print ("Yes your guess is correct")
        print ("------------------------------------")
    elif (L-2 <= n <= L+2):
        print ("------------------------------------")
        print ("You are almost there")
        print ("------------------------------------")
    elif (L-2 < n < 25) :
        print ("------------------------------------")
        print ("You are too high")
        print ("------------------------------------")
    elif (L+2 > n > 1):
        print ("------------------------------------")
        print ("You are too low")
        print ("------------------------------------")
    else:
        print ("------------------------------------")
        print ("Incorrect Number given as input !!! ")
        print ("------------------------------------")
#Main here
almost()
