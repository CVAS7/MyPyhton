"""
S14Q03
Ask the user to enter any 10 numbers as input.
Randomly pick any 5 numbers from this list
  but print them in the same order as given by the user.
"""
import random
from random import randint
num = raw_input("Enter the ant 10 numbers as input:")
list1 = [int(num)]
cnt = 0
while cnt < 9:
    num = raw_input("Enter the ant 10 numbers as input:")
    list1.append(int(num))
    cnt += 1
print "Input numbers:         ",list1
list2 = list1[:]
sub1 = random.sample(list1,5)
print "Random 5 number pick:  ",sub1
for i in sub1: list1.remove(i)
for i in list1: list2.remove(i)
print "Random 5 in same order:",list2
