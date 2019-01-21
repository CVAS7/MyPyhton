"""    

Ask the user to enter a number.
- If the number is a single digit number, add 7 to it, 
     and print the number in its unit’s place
- If the number is a two digit number, raise the number to the power of 5, 
     and print the last 2 digits
- If the number is a three digit number, ask user to enter another number. 
     Add the 2 numbers and print the last 3 digits
add
unitplace
power5
digitcheck
"""

def addn(n1,n2=7):
    sum1 = n1+n2
    units(str(sum1))

def units(n1):
    print n1[-1:]

def powern(n1,n2):
    p = pow(n1,n2)
    units(str(p))

def askother(n1):
    n2 = raw_input("Enter the 2nd Number:")
    s=addn(n1,int(n2))

def Digitscheck(n):
    if len(n) == 1:
        addn(int(n))
    elif len(n) == 2:
        powern(int(n),n2=5)
    elif len(n) == 3:
	askother(int(n))
    else:
        print n #Printing number as is

#Main
n1 = raw_input("Enter a number:")
Digitscheck(n1)
