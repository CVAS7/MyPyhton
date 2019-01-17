"""- Print the multiplication table of a given number using for and while loops"""
n = input("Enter a number for which Multiplication table is required:")
i = 0
while i <= 10:
    for i in range(i,11):
        print n,'x',i,'=',i*n
        i += 1
