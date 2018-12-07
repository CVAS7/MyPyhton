#!/usr/bin/python
eng = input("Enter Marks in English:")
sci = input("Enter Marks in Science:")
mat = input("Enter Marks in Maths:")
def per(a,b,c):
    per1 = ((a+b+c)/3)
    return per1

def check(d):
    if (d>=90):
        print "Your Grade is A"
    elif (90 > d >= 80):
        print "Your Grade is B"
    elif (80 > d >= 35):
        print "You are Average"
    else:
        print "You are Fail"
#Main Here
#percentage =  per(eng,sci,mat)
check(per(eng,sci,mat))
