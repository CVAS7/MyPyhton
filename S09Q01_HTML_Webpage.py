"""
S09Q01
Write a program that generates a HTML webpage.
Prompt the user for webpage title and webpage body contents.
The webpage body should contain
 - one main header,
 - one sub header, and
 - at least 2 paragraphs.
A sample output is shown below :
"""
name = raw_input("Enter the name of the html:")
title = raw_input("Enter the document tile:")
bodymainhead = raw_input("Enter the Main header:")
body1 = raw_input("Enter the paragraphs:")
body2 = raw_input("Enter the paragraphs:")
if len(body1) >= 20:
    body1 = body1[0:20]+"\n"+"    "*3+body1[20:]
    body2 = body2[0:20]+"\n"+"    "*3+body2[20:]
print "   "*20+name+".html"+"   "*20
print "<html>"+"\n"+"   "+"<head>"+"\n"+"   "*2+"<title>"+"\n"+"    "*3+title+"\n"+"   "*2+"</title>"+"\n"+"   "+"</head>"+"\n"*2+"   "+"<body>"+"\n"+"    "*2+"<h1>"+bodymainhead+"</h1>"
print "    "*2+"<p>"+body1+"\n"+"    "*2+"<\p>"+"\n"
print "    "*2+"<p>"+body2+"\n"+"    "*2+"<\p>"+"\n"
print "   "+"</body>"+"\n"+"</html>"
