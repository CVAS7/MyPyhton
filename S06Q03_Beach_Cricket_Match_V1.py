"""
S06Q03 : Beach Cricket Match
     - Collect the names of the 2 batmen currently playing.
              Who among them is currently at the non strikers end ?
          - Collect runs scored for each ball.
              Make sure, you accumulate runs for the correct player
                   based on who is facing the ball.
          - Remember that players change positions at the end of each over.
          - The match ends after 30 balls, or
               - if any batsman scores more than 60 runs.
          - Print all the statistics for each batsman
               as was done for the earlier T20 match [ S06Q02 ]
"""

def swap(str1):
    if str1 == A:
        Stricker = B
    else:
        Stricker = A
    return Stricker


Bat1 = raw_input("Enter the Name of Stricker:")
Bat2 = raw_input("Enter the Name of Non Stricker:")
Stricker,Score,A,B = [],[],[],[]
Stricker = A
for over in xrange(0,5):
    for Balls in xrange(0,6):
        if sum(A) >= 60 or sum(B) >= 60:
            if sum(A) >= 60:
                print "Match over due to ",Bat1,"Scored 60+"
            else:
                print "Match over due to ",Bat2,"Scored 60+"
            break
        BallStatus = raw_input("Enter the Current ball status Should be any number in [0,1,2,3,4,6]:")
        Score.append(int(BallStatus))
        Stricker.append(int(BallStatus))
        if ((Score[Balls] == 1 or Score[Balls] == 3) and Balls < 6):
            Stricker = swap(Stricker)
        elif (Balls == 6 and (Score[Balls] == 0 or Score[Balls] == 2 or Score[Balls] == 4 or Score[Balls] == 6)):
            Stricker = swap(Stricker)
        Total_Runs = sum(Score)
        print "Current Over:",over
    
print "Total Score",sum(Score)
print "Match Over:Balls Bowlled are",len(Score)
print "="*50
print "Scores of",Bat1,"::::::::"
print "Runs Scored",sum(A)
print "Number of Fours:",A.count(4)
print "Number of Sixs:",A.count(6)
print "Number of Dot Balls",A.count(0)
print "Strike rate:", float(sum(A)/len(A))
print "="*50
print "Scores of",Bat2,"::::::::"
print "Runs Scored",sum(B)
print "Number of Fours:",B.count(4)
print "Number of Sixs:",B.count(6)
print "Number of Dot Balls",B.count(0)
print "Strike rate:", float(sum(B)/len(B))
