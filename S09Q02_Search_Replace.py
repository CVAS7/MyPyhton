"""
Write a search and replace program in Python.
This should first take the original text as input by prompting the user for it.
It should then, prompt the user for which word to search,
and what new word it should be replaced with.
"""
text = raw_input("Enter the test:")
tofind = raw_input("Enter the word to find:")
toreplace = raw_input("Enter the word to replace:")
print text
print text.replace(tofind,toreplace)
