"""
Write a search and replace program in Python.
This should prompt the user for which word to search,
  and what new word it should be replaced with.
The file to be modified should be taken as argument to this program
"""
#text = raw_input("Enter the test:") 
tofind = raw_input("Enter the word to find:")
toreplace = raw_input("Enter the word to replace:")
tofile = raw_input("Enter the file name to Modifie:")
FH = open(tofile,"r")
all_text = FH.read()
print all_text
modifiedtext = all_text.replace(tofind,toreplace)
print modifiedtext
FH.close()
WFH = open(tofile,"a+")
WFH.write(modifiedtext)
WFH.close()
