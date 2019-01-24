""" Takes a filename as argument 
    Creates a new file with the name
    "shuffle" appended to the original filename.
    The lines in the input are shuffled 
    and written into the new file
"""

import os
from fileops import *
import sys
import random
from sys import argv

def shuffler(lines):
    """ Shuffle a list of strings Input : list of strings
    Return : a new list with original strings shuffled
    """
    print lines
    random.shuffle(lines)
#    shuff = open("shuffle", 'w').writelines(lines)
    print lines
    return lines


#def write_line(new_name, shuffled_lines):
#    open(new_name, 'w').writelines(shuffled_lines)

# Main starts here
# Get filename from command line
file = sys.argv[1]
FH = open(file,"r")
lines = get_lines(file) 
FH.close()



shuffled_lines = shuffler(lines)
print shuffled_lines
base=os.path.basename('/home/suresh/Malasani/Python/demofile5.txt')
base
file = os.path.splitext(base)[0]
new_name = file + "shuffle.txt"
write_lines(new_name, shuffled_lines)
