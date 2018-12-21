"""
A melting furnace converts a hollow sphere into a solid cylinder of 3cm diameter with a 5% loss.
Write a program that finds out the length of the solid cylinder when
 the inner and external radii of the hollow sphere are known
Volume of sphere = 4/3 * pi * r * r * r
Volume of cylinder = pi * r * r * height
"""
from math import pi as p
from math import pow as pa
CylinderHeightCm =  2
cyl_dia_cm = 3
sph_dia_cm = 3+(3*0.05)
print "VolumeSphere:",(4/3)*p*pa((sph_dia_cm/2),3)
print "VolumeCylinfer:",(p*(pa((cyl_dia_cm/2),2))*CylinderHeightCm)



==============================
Output:
VolumeSphere: 12.2741534102
VolumeCylinfer: 6.28318530718
