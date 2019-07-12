[suresh@localhost Practice]$ cat S19Q02_UnitTest.py
"""
Solve this question, only if you are feeling challenged enough to attempt it.
The data for 4 students of Sunflower School class X is shown below :

- Write a program that ranks the students
    based on the total of their marks in all
    the subjects for each unit test.

- Then, rank the students based on their
    total marks for all the tests using the below formula
    - Total marks = 25% Unit test + 75% Final

- Among unit tests, which student has
   scored the highest marks for each subject ?
   - Also mention the highest score for each subject

- Which is the subject where each student has scored his/her highest marks ?


- There was a printing mistake in Maths paper of the final exam.
    All the students who attempted that question are given 3 bonus marks.
    Sneha and Ashish have attempted that question.
    What are the new ranks now ?
"""
import glob
import sys
import os
from sys import argv
import time
path = sys.argv[1]
records = {}

def togetfilesnames(path):
    files = (glob.glob(path+"/*.txt"))
    lstudent = []
    for i in files:
        base=os.path.basename(i)
        StudentName = base.split('.')[0]
        lstudent.append(StudentName)
    return files,lstudent

def todict(files,lstudent,records):
    exams = ['unit1','unit2','unit3','final']
    subjects = []
    for f in lstudent:
        records[f] = {}
        for e in exams :
            records[f][e] = {}
    for i in xrange(len(lstudent)):
        FH = open(files[i],'r')
        all_lines = FH.readlines()
        for j in all_lines:
            k = j.strip().split(':')
            k1 = k[0].strip()
            v1 = k[1].strip().split(',')[0]
            v2 = k[1].strip().split(',')[1]
            v3 = k[1].strip().split(',')[2]
            v4 = k[1].strip().split(',')[3]
            records[lstudent[i]][exams[0]][k1] = int(v1)
            records[lstudent[i]][exams[1]][k1] = int(v2)
            records[lstudent[i]][exams[2]][k1] = int(v3)
            records[lstudent[i]][exams[3]][k1] = int(v4)
            if k1 not in subjects:
                subjects.append(k1)
#        print subjects
#    print records
    return records,exams,lstudent,subjects
def usecase(records,exams,lstudent,subjects,b):
    ranks,units = {},{}
    for e in xrange(len(exams)):
        if b != 'y' or exams[e] == 'final':
            print '-'*100
            print exams[e].title(),'Status:'
        for i in xrange(len(lstudent)):
            #print 'here',records[lstudent[i]][exams[e]].values()
            #print 'here 2',exams[e]
            ranks[lstudent[i]] = sum(records[lstudent[i]][exams[e]].values())
            if exams[e] == 'unit1' or 'unit2' or 'unit3':
                units[lstudent[i]] = (sum(records[lstudent[i]][exams[e]].values())*0.25)
            elif exams[e] == 'final':
                units[lstudent[i]] = (sum(records[lstudent[i]][exams[e]].values())*0.75)
            maxsubjectname = max(records[lstudent[i]][exams[e]].keys(),key=(lambda k: records[lstudent[i]][exams[e]][k]))
            if b != 'y' or exams[e] == 'final':
                print lstudent[i].title(),'Scored maximum marks in',maxsubjectname,'in',exams[e],'Exams among all the subjects','with',records[lstudent[i]][exams[e]][maxsubjectname]
        examsrank = max(ranks.keys(), key=(lambda k : ranks[k]))
        forsameranks = {}
        for i in xrange(len(ranks.keys())):
            if ranks.values()[i] == ranks[examsrank]:
                k1 = ranks.keys()[i]
                forsameranks[k1] = ranks.values()[i]
        if len(forsameranks) == 1:
            if b != 'y' or exams[e] == 'final':
                print '-'*100
                print forsameranks.keys()[0].title(),'ranked 1 with',forsameranks.values()[0],'marks in',exams[e],'Exams'
            elif b != 'y' or exams[e] == 'final':
                print '-'*100
                print forsameranks.keys()[0].title(),'and',forsameranks.keys()[1].title(),'ranked 1 with',forsameranks.values()[0],'marks in',exams[e],'Exams'
    for s in xrange(len(lstudent)):
        finalranks = max(units.keys(), key=(lambda k : units[k]))
        print finalranks.title(),'Ranked',s+1,'with aggeration marks',units[finalranks]
        del units[finalranks]
    
def subjectranks(records,exams,lstudent,subjects):
    subjectranks,subtop = {},{}
#    for i in xrange(len(records.keys())):
    for s in subjects:
        subtop[s] = {}
        for e in exams:
            subtop[s][e] = {}
            for n in lstudent:
                subtop[s][e][n] = {}
    print 'Subject Wise Ranking:'
    print '-'*100
    for s in subjects:
        for e in exams:
            tmp = {}
            print '-'*100
            print 'For Subject:',s.title(),'In',e.title()
            print '-'*100
            for n in lstudent:
#                print s,e,n,'-',records[n][e][s]
                tmp[n] = records[n][e][s]
            maxmark = max(tmp.keys(),key=(lambda k : tmp[k])) 
            print maxmark.title(),'has topped in',s,'in',e,'Exams with',tmp[maxmark],'Marks'
b = 'n'    
f,p = togetfilesnames(path)
r,e,s,sub = todict(f,p,records)
subjectranks(r,e,s,sub)
usecase(r,e,s,sub,b)
print 'Any printing mistake in Maths paper'
try:
    b =  raw_input('Enter yes or no:')
    if b == 'y' or b ==  'Y' or b == 'Yes' or b == 'yes':
        b = 'y'
#    print 'Enter Student name who got printing mistakes with comma(,) separated'
        pmistake = raw_input(['Enter Student name who got printing mistakes with comma(,) separated'])
        pmistake = pmistake.split(',')
        for p in pmistake:
            p = p.lower()
            newmarks = records[p]['final']['maths']+3
            records[p]['final']['maths'] = newmarks
        print '-'*100
        print "New final ranks after addition of 3 Marks"
        usecase(records,e,s,sub,b)

    else:
        print 'bye.....'
except:
    print "bye....."
    sys.exit()
