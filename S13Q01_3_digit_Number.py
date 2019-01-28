"""
Ask the user to enter a 3 digit number, till he enters 0. 
Discard all numbers that are not 3 digit numbers. 
From all the 3 digit numbers entered by the user, 
     find and print the prime numbers in descending order.
"""
# Python program to check if the input number is prime or not
# take input from the user
# num = int(input("Enter a number: "))

# prime numbers are greater than 1
def primecheck(num):
    if num > 1:
   # check for factors
        for i in range(2,num):
            if (num % i) == 0:
                break
        else:
            return num
       
# if input number is less than
# or equal to 1, it is not prime
#    else:
#       print(num,"is not a prime number")

#main
if __name__ == "__main__":
    numbers,prime = [],[]
    innum = int(raw_input("Enter the 3 digit number and Enter 0 for Exit:"))
    if innum != 0:
        numbers.append(innum)
    while innum != 0:
        innum = int(raw_input("Enter the 3 digit number and Enter 0 for Exit:"))
        if innum != 0:
            numbers.append(innum)
    print "Numbers:",numbers
    for i in numbers:
        if (99 < i <= 999):
            a =  primecheck(i)
            if a != None:
                prime.append(a)
    print "Prime Numbers",prime
