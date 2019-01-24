import sys
from sys import argv
fname = sys.argv[1]
from fileops import get_line,max_line
import random
from random import randint
a = max_line(fname)
a1 = random.randint(0,a-1)
b = get_line(fname,a1)
