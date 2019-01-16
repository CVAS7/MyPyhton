#!/usr/bin/python
eng = input("Enter Marks in English:")
if (0 <=  int(eng) <= 75):
    sci = input("Enter Marks in Science:")
    mat = input("Enter Marks in Maths:")
else:
    print ("Max mark for English is 75")
    eng = input("Enter Marks in English:")
    sci = input("Enter Marks in Science:")
    mat = input("Enter Marks in Maths:")
def per(a,b):
    per1 = ((a/b)*100)
    return per1

def check(x,y,z):
    if (x >= 90 and y >= 90 and z >= 90):
        print "Your Grade is A"
    elif (90 > x >= 80 and 90 > y >= 80 and 90 > z >= 80):
        print "Your Grade is B"
    elif (x < 35 or y < 35 or z < 35):
        print "You are Fail"
    else:
        print "You are Average"
#Main Here
percentageE =  per(eng,75.0)
percentageS =  per(sci,90.0)
percentageM =  per(mat,100.0)

check(percentageE,percentageS,percentageM)
