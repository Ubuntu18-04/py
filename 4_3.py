even=odd=0
l=int(input("Enter the number of bottles:"))
for x in range(1,l+1):
    a=int(input("Enter the number of pebbles in bottle:"))
    if a%2==0:
        even+=1
    else:
        odd+=1
print("The number of Even bottles=",even,"\nThe number of odd bottles=",odd)