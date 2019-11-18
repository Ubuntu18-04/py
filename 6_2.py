n=(input("Enter the number to be checked"))
ch=di=sp=0
for x in range(len(n)):
    if n[x].isalpha():
        ch+=1
    elif n[x].isdigit():
        di+=1
    else:
        sp+=1
print("The number of characters in string",ch,"Digits=",di,"special characters=",sp)