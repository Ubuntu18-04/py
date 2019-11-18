lst=ls=[]
n=eval(input("Enter the length string"))
c=0
for i in range(0,(n)):
    ele=str(input())
    lst.append(ele)
for i in lst:
    if len(i)>=2 and i[0]==i[len(i)-1]:
        c+=1
        ls.append(i)
print("The strings satisfying the conditions are:",c)
print(ls)
