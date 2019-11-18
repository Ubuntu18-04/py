import math as m
a=int(input("Enter the length of the first side:"))
b=int(input("Enter the length of the second side:"))
c=int(input("Enter the length of the third side:"))
s=(a+b+c)/2
area=m.sqrt(s*(s-a)*(s-b)*(s-c))
print("Area of triangle=",area)