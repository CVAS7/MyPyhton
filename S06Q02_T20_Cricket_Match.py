"""
S06Q02 : T20 Cricket Match
     - Collect the runs scored for each ball faced by the batsman.
              A dot ball is represented by a dot in input.
              An empty line represents a wicket.
          - Find the total runs scored by the batsman
          - Find the strike rate of the batsman [ runs scored/balls faced ]
          - Find the number of balls wasted by the batsman
          - How many boundaries and sixes did he score ?
"""

def scores(Batsman):
    b,b1 = "Some",""
    while b != "":
        b = ""
        b = raw_input("Enter the Current Ball status:")
        b1 = b1+" "+b
    return b1.split()
def runs(Data):
    dot,four,six,total = 0,0,0,0
    for i in Data:
        if i != '.':
            total = total+int(i)
            if int(i) == 4:
                 four += 1
            elif int(i) == 6:
                 six += 1
        else:
            dot += 1
    balls = len(Data)
    strike = float(total/balls)
    print ("Total Score of Bastman:",total)
    print ("Number of Dot balls:   ",dot)
    print ("Number of bounaries:   ",four)
    print ("Number of sixes:       ",six)
    print ("Strike rate:           ",strike)
    return total,dot,four,six,strike

#Main  
A = "Vir"
Vir = scores(A)
runs(Vir)
