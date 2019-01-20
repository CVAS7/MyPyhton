"""
S07Q01
Get the users first name and last name. 
        Assume the user provides Dharmender and Singh as inputs, 
          then print the users name in the following order and format
        - Name : dharmender, Surname : singh 
        - DHARMENDER SINGH
          ---------------------  ---------
        - Dharmender, Singh

"""
fname = raw_input("Enter first name:")
lname = raw_input("Enter last name:")
print "Name :",str.lower(fname),",","Surname :",str.lower(lname)
print str.upper(fname)+" "+str.upper(lname)
print "-" * 21,"  ","-" * 9
print (str.upper(fname[0]))+(str.lower(fname[1:]))+",",(str.upper(lname[0]))+(str.lower(lname[1:]))
