"""
Ask user to enter the students name followed by his total marks in the SSLC exam.
An empty line indicates the end of input.
Print the names and marks of all students
    who have scored more than 90% marks,
    in ascending order of their marks.
"""
record,all_records = [],[]
r,r1 = 0,0
while r1 != "":
    record = []
    r = r+1
    r1 = raw_input("Enter the name of the sutudent:")
    if r1 == "":
        break
    r2 = raw_input("Enter the Total marks obtained:")
    r3 = round(((float(r2)/625)*100),2)
    a = [r,r1,r2,r3]
    record.append(a)
    all_records.append(a)
    print "sublist",a
    print "list",all_records
all_records.sort(key=lambda list:float(list[3]),reverse=True)
print "[Sno,Name,Marks,Percentage]"
for i in all_records:
    if i[3] >= 90:
        print i
