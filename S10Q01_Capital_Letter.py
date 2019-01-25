"""
Get the name of the text file from the user.
Check if all the sentences in that text file begin with a capital letter.
"""
# You have three options for punctuating the end of a sentence: a period(.) an exclamation mark(!) or a question mark(?)
fname = raw_input("Enter the file name:")
FH = open(fname,"r")
x = FH.readlines()
for i in xrange(len(x)):
    print x[i][:1]
    if str(x[i][:1]) == str.upper(x[i][:1]):
        print "line:",i,"begin with a capital letter that is",str(x[i][:1])
    else:
        print "line:",i,"Does not begin with a capital letter that is",str(x[i][:1])
FH.close()

