#!/usr/bin/python
#print the first 10 fibonacci numbers
r = range (1,50)
n1,n2,cnt = 1,2,0
for i in r:
    n3 = n1+n2
    n1 = n2
    n2 = n3
    if n3%2 == 0 and cnt < 12:
        cnt += 1
        print n3


Output:

[suresh@localhost Python]$ python Fibonacci_Even12.py
8
34
144
610
2584
10946
46368
196418
832040
3524578
14930352
63245986
