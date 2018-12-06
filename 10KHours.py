#!/usr/bin/python
L = 10000
n = input("Number of hours a day you can dedicate for python: ")
#days = L/n
#hours = L%n
#months = days/30
#days = months%30
#years = months/12
#months = years%12

#print "You need ",years," years",months," months",days," days",hours," hours to be Master in writing a code"

def calc(a,b):
    div1 = a /b
    mod1 = a % b
    return (div1,mod1)
def calc2(c,d):
    div2 = c/d
    mod2 = div2%d
    return (div2,mod2)


#Main here
days,hours = calc (L,n)
months,days = calc2(days,30)
years,months = calc2(months,12)
print "=============================="
print "As per 10,000 Hours Rule \nYou need ",years," years",months," months",days," days",hours," hours to be Master in writing a code"
print "=============================="
