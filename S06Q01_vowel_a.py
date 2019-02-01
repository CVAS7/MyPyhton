"""
S06Q01
     - Write a program that takes multiple sentences as input from the user. 
          The last input is indicated by an empty line.
          - Find the number of words entered
          - Find the number of words that contain the vowel a
"""
def vowel(string):
    str1 = string[1:(len(string)-1)]
    for z in str1:
        if 'a' in z:
            print (z,"Contains a")


input1 = 'somthing'
word = ''
#word = raw_input("Enter a sentences:")
while input1 != '':
    input1 = ''
    input1 = raw_input("Enter a sentences:")
    word = word+" "+input1

vowel(word.split(" " ))
