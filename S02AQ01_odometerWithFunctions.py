"""
    Re-write the earlier question of S02Q02 using functions :
     - Using the starting and ending values of your car`s odometer, 
            calculate its mileage
            """
def start():

    startRead = input("Enter the Start Reading")
    return startRead

def end():
    endRead = input("Enter the End Reading")
    return endRead

def dist():
    DistTra = input("Enter Kms Travled")
    return DistTra

def Mileage():
    s = int(start())
    e = int(end())
    d = int(dist())
    M = ((e-s)/d)
    return M

# Main Here
M = Mileage()
print M
