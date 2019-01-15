"""     - Take 2numbers from the user. 
            Print which number is a 2 digit number, 
            and which number is a 3 digit number. 
            If it is neither, then print the number as it is"""

def Digitscheck(n):
    if len(n) == 2:
        print ("Number of digits for",n,"is 2")
    elif len(n) == 3:
        print ("Number of digits for",n,"is 3")
    else:
        print n #Printing number as is

#Main
n1 = raw_input("Enter a number:")
n2 = raw_input("Enter another number:")
Digitscheck(n1)
Digitscheck(n2)
