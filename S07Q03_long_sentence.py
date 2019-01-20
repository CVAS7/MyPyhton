"""
S07Q03
Prompt the user to enter a long sentence
        - What is the last character in the sentence ?
        - What are the last 5 characters in the sentence ?
        - Print the characters that are present in 2nd and 5th position of the sentence
        - Print the character at the center of the string, along with the 2 adjoining characters.
        Ex : If the string entered is Web Browser
        the character at its centre is r and so print Bro
"""

sentence = raw_input("Enter the long sentence:")
print "last character",sentence[-1]
print "last 5 characters",sentence[-5:]
print "2nd position character",sentence[3],"3rd position character",sentence[6]
print "center and 2 adjoining characters",sentence[(len(sentence)/2):(len(sentence)/2)+3]
