import math as m
n=eval(input("Enter the number"))
count=c=0
a=0 
b=1
x=m.sqrt(n)
if (int(x+0.5)**2)==n:
    print("The number",n," is a perfect square")
else:
    print("The number ",n," is not a perfect square")
while n!=1:
    if n%2!=0:
        break
    c+=1
    n//=2
    count=1
if count==1:
    print("THe number ",n," is a perfect power of 2")
else:
    print("The number ",n," is not a perfect power of 2")
count=0
for i in range(1,n+1):
    temp=a+b
    a=b
    b=temp
    if temp==n:
        count+=1
        break
    else:
        continue
if count==1:
        print(n," Is present in a fibonacci series")
else:
        print(n," is not present in a fibonacci series")