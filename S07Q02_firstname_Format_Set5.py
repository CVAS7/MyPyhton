"""
S07Q02
Get the users first name and last name. 
        Assume the user provides Dharmender and Singh as inputs, 
        Find his best possible initials by eliminating the last character 
        from each of the name as shown in this sample output
        - Step 1 : Dharmender Singh
        - Step 2 : Dharmende Sing
        - Step 3 : Dharmend Sin
        - Step 4 : Dharmen Si
        - Step 5 : Dharme S

        Expected output :
        Best possible initials of Dharmender Singh is :
        Dharme S
"""
fname = raw_input("Enter first name:")
lname = raw_input("Enter last name:")
print "Step 1 : "+fname,lname
i = 1
while i <= 4:
    print "Step",i+1,": "+fname[:len(fname)-int(i)],lname[:len(lname)-int(i)]
    i +=1
