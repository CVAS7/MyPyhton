import sys
from sys import argv
def filenamechange(fname,newfilename):
    changedfilename = newfilename
    print changedfilename
    return changedfilename

def readfile():
    text = FH.read()
    lines = text.split("\n")
    for i in xrange(0,len(lines)-1):
        print i
        if (i) == 0:
            addlines(lines[i])
            addlines("\n")
            
        elif ((i)%2 != 0):
            print lines[i],"\n",lines[i]
            addlines(lines[i])
            addlines("\n")
            addlines(lines[i])
            addlines("\n")
        elif ((i)%2 == 0):
            addlines(lines[i])
            addlines("\n")
    addlines(lines[0])


def addlines(lines):
    WFH = open(sys.argv[2],"a")
    WFH.write(lines)
    WFH.close()






#Main
newfile = filenamechange(sys.argv[1],sys.argv[2])
if len(argv) < 2:
    print "please pass the argv","\n","Example: python t12 <oldfilename> <newfilename>"

FH = open(sys.argv[1],"r")
readfile()
FH.close()
