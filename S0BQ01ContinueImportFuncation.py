"""
Write a Python function, that asks the user if he wants to continue. 
It should print continue and return True, if the user types in a yes,
irrespective of the case in which yes is typed. 
Import this function in any of your earlier exercises and 
run that exercise in a loop as long as the user enters No
"""
def ask():
    print "Do you want to Continue:"
    a = raw_input()
    if a.upper() == "YES":
        print "Continue"
        return True
#Main Here
if __name__ =="__main__":
    b = ask()
    print b
