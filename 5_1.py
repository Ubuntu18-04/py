n=eval(input("Enter the number to check for factors and check whether it is prime or composite:"))
c=0
l=[]
for x in range(1,(n//2)+1):
    if n%x==0:
        c+=1
        l.append(x)
if c>1:
    print("The number is composite")
else:
    print("The number is prime")

print("The factors are",l)