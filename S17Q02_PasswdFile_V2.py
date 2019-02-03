"""
Read passwd file and list all users mentioned in that file in ascending order of their user id.
Also mention the users real name and home directory in the output.
A sample passwd file is shown below :

header for passwd file heads:
Username:Password:User ID (UID):Group ID (GID):User ID Info:Home directory:Command/shell    
"""

#!/usr/bin/env python

FH = open("/etc/passwd", 'r')

dict1 = {}
for line in FH:
    value1 = line.strip().split(":")
    dict1[int(value1[2])] = value1[5]
FH.close()
print "User ID (UID)","=>","Home directory"
for u in sorted(dict1.keys()):
    print u,"=>",dict1[u]  
    
    
