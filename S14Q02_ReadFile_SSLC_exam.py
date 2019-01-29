"""
S14Q02
Create a text file called students.txt.
Each line should be of the form
student_name : student_marks
- Write a Python program to read the contents from this file.
- Print the names and marks of all students
      who have scored more than 90% marks,
      in ascending order of their marks.
"""
records,record,a =[],[],[]
FH = open("students.txt","r")
all_text = FH.read()
all_lines = all_text.split("\n")
records = all_lines
FH.close()

a = records[0].split(":")
a.append(" Percentage ")
records[0] = a

for i in xrange(1,len(records)-1):
    e = float(records[i].split(":")[1].strip())/625
    e = round(e*100,2)
    b = records[i].split(":")
    b.append(e)
    records[i]=b
c=records[-1]
records.remove(c)
r = records[0]
records.remove(r)
records.sort(key=lambda list:float(list[2]),reverse=True)
records.insert(0,r)
#print records
for i in records:
    print i
