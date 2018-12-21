"""
Like everyone I too enjoyed watching Taj Hotel from Mumbais Gateway of India.
When I stood at the Gateway of India, I saw that the
top of Taj Hotels tower was at an angle of elevation of 25 degrees.
I then walked to the security guard near the gate of Taj Hotel and
noticed that the top of the tower was at an angle of elevation of 65 degrees.
The security guard informed me that the Tower was about 100 yards from the gate.
Write a program to find the height of Taj Hotels tower and
the distance between Gateway of India and Taj Hotels entrance.
"""



from math import sin, cos, tan, radians
DisGateToTowerYards = 100
GatewayAngleA = 25
GatewayAngleB = 65
TowerHeightinYards = 100*tan(radians(25))
TajHotelsEntranceToTowerinYards = TowerHeightinYards/tan(radians(65))
GatewayofIndiaToTajHotelsEntranceinYards = DisGateToTowerYards - TajHotelsEntranceToTowerinYards
print "TowerHeightinYards:",TowerHeightinYards
print "TajHotelsEntranceToTowerinYards:",TajHotelsEntranceToTowerinYards
print "GatewayofIndiaToTajHotelsEntranceinYards",GatewayofIndiaToTajHotelsEntranceinYards
========
Output:

TowerHeightinYards: 46.6307658155
TajHotelsEntranceToTowerinYards: 21.7442832054
GatewayofIndiaToTajHotelsEntranceinYards 78.2557167946

