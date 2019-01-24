
def get_lines(filename):
    """ Reads the contents of filename
        and returns the - File handle
        - List of all lines of the file
    """
    ## Your implementation goes here ###
    FH = open(filename,"r")
    print "="*10
    all_text = FH.read()
    all_lines = all_text.split('\n')
    print all_lines
    print "="*10
    print all_text
    print "="*10
    for l in all_lines:
        print l
    print "="*10
    return all_lines
    


def write_lines(filename, lines):
    """ Writes the lines into the a file whose
        filename is given as argument
    """
    ## Your implementation goes here ###
    print "="*10
    FH = open(filename,"a+")
#    FH.write(lines)
    for l in lines:
         FH.write(l)
    FH.close()
   
def get_line(filename,linenumber):
    FH = open(filename,"r")
    print "="*10
    b1 = FH.readlines()[linenumber]
    print b1
    print "="*10

def max_line(filename):
    num_lines = sum(1 for line in open(filename))
    return num_lines

# Main
if __name__ == "__main__":
    x = get_lines("demofile.txt")
    b = write_lines("demofile2.txt",x)
