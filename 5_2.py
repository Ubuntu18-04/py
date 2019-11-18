n=eval(input("Enter the number to check if perfect"))
c=0
for x in range(1,(n//2)+1):
    if n%x==0:
        c+=x
if c==n:
    print("The number",n,"is perfect")
else:
    print("The number",n,"is not perfect")