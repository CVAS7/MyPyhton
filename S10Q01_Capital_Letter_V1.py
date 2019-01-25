Get the name of the text file from the user.
Check if all the sentences in that text file begin with a capital letter.
"""
# You have three options for punctuating the end of a sentence: a period(.) an exclamation mark(!) or a question mark(?)
import re
fname = raw_input("Enter the file name:")
FH = open(fname,"r")
x = FH.read()
a = re.split(r'[.!?]', x)
for i in xrange(len(a)):
    print a[i]
    if str(a[i][0]) == str.upper(a[i][0]) and (a[i][0]) != "\n":
        print "line:",i+1,"begin with a capital letter that is",str(a[i][0])
    else:
        print "line:",i+1,"Does not begin with a capital letter that is",str(a[i][:10])
FH.close()
