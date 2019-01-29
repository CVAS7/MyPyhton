"""
S15Q02
Write a function that accepts 2 lists as arguments.
Both these 2 lists must be already sorted in the ascending order
This function should combine the lists into a sorted order and return the resulting list.
This function should not use any built-in sort function or method.
- Write a test function that will test that the sorted list is correct.

After successfully testing your program,
    pass the following 2 lists as arguments to your function
    and print the sorted result.

    - left  = [4, 17, 21, 47, 69, 75, 91, 97]
   - right = [3, 10, 11, 14, 18, 21, 44, 55, 76,97]
"""
import sys,ast
from sys import argv


def SortAscending(list1,list2):
    l3 = list1+list2
    print "l3",l3
    l4=[]
    for i in xrange(len(l3)):
        l4.append(min(l3))
        l3.remove(min(l3))
    return l4

def sortfunction(list1,list2):
    l3 = list1+list2
    l3.sort()
    return l3



#Main
l1 = ast.literal_eval(sys.argv[1])
l2 = ast.literal_eval(sys.argv[2])
l4 = SortAscending(l1,l2)
print "After Sorting in Ascending order",l4
l5 = sortfunction(l1,l2)
print "With Functions                  ",l5
