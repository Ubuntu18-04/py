ls=list(input("Enter the string").split(" "))
l=[]
for i in ls:
    l.append(i[::-1])
for i in l:
    print(i,end=" ")
