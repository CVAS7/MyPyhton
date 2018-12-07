#!/usr/bin/python
start = input ("please enter stating reading of odometer:")
end = input ("please enter ending reading of odometer:")
fuelstart = input ("Enter fuel reading at the Starting of your Trip:")
fuelend = input ("Enter fuel reading at the ending of your Trip:")

def odoread (r1,r2):
    Dist = r2 - r1
    return Dist

def fueluseage (f1,f2):
    FuelBurn = f1 - f2
    return FuelBurn
def mileage1(d1,f3):
    mileage = d1 / f3
    return mileage

#Main is here
print "======================================="
Dist1 = odoread(start,end)
print "Distance Travelled:", Dist1
FuelUsed = fueluseage (fuelstart,fuelend)
print "Fuel used in your trip is:", FuelUsed 
Mileage = mileage1(Dist1,FuelUsed)
print "Your car mileage is:", Mileage
#stops = 560/Mileage
NumberOfLiterRequired = 560/Mileage
CarTankCapacity = 45
stops = NumberOfLiterRequired/CarTankCapacity
print "Number of stops one should make for refuelling while travelling from Bangalore to Goa is ", stops
