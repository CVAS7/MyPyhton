#!/usr/bin/python
sales = range (94,108)
for i in sales:
    i = float(i)
    if (94 <= i <= 99):
        print float(i/2)
    else:
        i = int(i)
        print i*2
