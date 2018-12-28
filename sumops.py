"""
Write a Python program sumops.py that contains a function called dsum.
This function takes a number as argument.
It returns the sum of its digits.
Write a test program that will test this function.
    - Write another Python program jackpot.py.
      It should ask the user to enter a 5 digit number,
      but only if the user has not provided it as an argument to jackpot.py
   - This program should use the dsum function by importing it
      from sumops.py to calculate the sum of all the digits of
      the 5 digit number provided by the user.
   - Now, generate a random number from 1 to 50.
   - If the sum of the digits matches this random number,
      the user wins the jackpot.
   - If not, then print the random number.
   """
import sys
def dsum(n=1111):
    result = 0
    for i in range(len(str(n))):
        result = result + int(str(n)[i:i+1])
    return(result)

#Main here
if __name__=="__main__":
    n = sys.argv[1]
    number = dsum(n)
    print "Sum of Digits in",n,"is",number
#number = dsum()
#print number
===========================================================
===========================================================
===========================================================
[suresh@localhost Python]$ python sumops.py 1111
Sum of Digits in 1111 is 4
[suresh@localhost Python]$ python sumops.py 11111
Sum of Digits in 11111 is 5

