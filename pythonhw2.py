import math
xA = float(input('Enter X coordinate of A:'))
yA = float(input('Enter Y coordinate of A:'))
xB = float(input('Enter X coordinate of B:'))
yB = float(input('Enter X coordinate of B:'))
xC = float(input('Enter X coordinate of C:'))
yC = float(input('Enter X coordinate of C:'))


AB = math.sqrt((xA - xB) ** 2 + (yA - yB) ** 2)
BC = math.sqrt((xB - xC) ** 2 + (yB - yC) ** 2)
AC = math.sqrt((xA - xC) ** 2 + (yA - yC) ** 2)

if AB + BC >= AC or AC + BC >= AB:
    AngleA = (math.acos(((AC**2) + (AB**2) - (BC**2)) / (2 * AC * AB))) * (180 / math.pi)
    AngleB = (math.acos(((AB**2) + (BC**2) - (AC**2)) / (2 * BC * AB))) * (180 / math.pi)
    AngleC = (math.acos(((BC**2) + (AC**2) - (AB**2)) / (2 * BC * AC))) * (180 / math.pi)
else:
    print("Invalid Coordinates For Traingle")

print("The angle alpha is:", AngleA)
print("The angle Beta is :", AngleB)
print("The angle Gamma is:", AngleC)
