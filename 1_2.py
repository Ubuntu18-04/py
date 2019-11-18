#Mr. Ashok dug a borewell just without any measurement but somehow was able to get the radius of the borewell.
#Now he wants to find the area and perimeter of the well. So help Ashok for the same

import math as m
m.pi
r=int(input("Enter the radius of the borewell:"))
d=int(input("Enter the depth of the borewell:"))
area=2*(m.pi*r*d+m.pi*r*r)
perimeter=2*(2*r*m.pi + 2*d)
print("The area of the cylinder=",area)
print("The perimeter of the cylinder=",perimeter)