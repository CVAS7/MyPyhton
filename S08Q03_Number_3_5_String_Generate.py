"""
S08Q03
Ask the user to enter a number.
- If the user enters a number as 5, then
generate the following string :
- 00001111222233334444
- If the user enters the number as 3, then
generate the following string :
- 001122
"""
number = raw_input("Enter the number:")
if int(number) == 5:
    print "0"*(int(number)-1)+"1"*(int(number)-1)+"2"*(int(number)-1)+"3"*(int(number)-1)+"4"*(int(number)-1)
elif int(number) == 3:
    print "0"*(int(number)-1)+"1"*(int(number)-1)+"2"*(int(number)-1)
else:
    print "Your input number is neigther 3 nor 5"
