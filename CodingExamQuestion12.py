"""
Brilliant School conducts an exam in subjects of English, Science and Mathematics.
Science exam is split up as Science Theory and Science Practical
The maximum marks for each subject is as follows :
          -- English : 75 marks
          -- Science Theory : 75 marks
          -- Science Practical : 25 marks
          -- Science = Science Theory + Science Practical : 100 marks
          -- Mathematics : 100 marks

The pass marks for each subject is as follows :
          -- Pass marks for English : 25
          -- Pass marks for Science Theory : 25
          -- Pass marks for Science Practical : 8
          -- Pass marks for Science : 35
          -- Pass marks for Mathematics : 35

Write a Python program to collect the marks scored by a student in all the above 4 exams
Based on the marks scored by the student, grade them according to the following criteria :
          -- Grade A : if Total > 90%
          -- Grade B : if Total > 75%
          -- Fail is any score is less than pass marks
          -- Average otherwise

Note : A student who scores only Pass marks in Science Theory and Science Practical
            will have a total of 33 [ 25 + 8 ]
            and this still falls short of the Pass marks for Science [ 35 ]
            and is considered as Fail.
"""
English= int(raw_input("Enter your English Maximun 75 marks:"))
ScienceTheory = int(raw_input("Enter your Science Theory Max 75 marks :"))
SciencePractical = int(raw_input("Enter your Science Practical Max 25 marks :"))
Mathematics  = int(raw_input("Enter your Mathematics Max 100 marks :"))


def PassFail(Eng,SciTh,SciPr,Mat):
    if (Eng >= 25 and SciTh >= 25 and SciPr >= 8 and SciTh+SciPr >= 35 and Mat >= 35):
        Sci = SciTh+SciPr
        per1 = Per(Eng,Sci,Mat)
        return per1
    else:
        print "Your considered as Fail"
        
def Per(Eng,Sci,Mat):
    per1 = ((Eng/75.0)*100+((Sci)/100.0)+(Mat/100.0))
    print per1
    if per1 >= 90:
        print "Your Gained Grade A"
    elif 90 >= per1 >= 75:
        print "Your Gained Grade B"
    elif per1 <= 75:
        print "Your are Average Student"

   

#Main here
per = PassFail(English,ScienceTheory,SciencePractical,Mathematics)

Output:


[suresh@localhost Python]$ python CodingExamQuestion12.py
Enter your English Maximun 75 marks:70
Enter your Science Theory Max 75 marks :70
Enter your Science Practical Max 25 marks :20
Enter your Mathematics Max 100 marks :90
95.1333333333
Your Gained Grade A
