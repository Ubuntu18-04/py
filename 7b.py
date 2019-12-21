n=int(input("size of the list"))
ls=[]
D={}
for i in range(0,n):
  i=int(input("enter num"))
  ls.append(i)
for i in ls:
    if(ls[i] in D):
      D[ls[i]]=D[ls[i]]+1
    else:
      D[ls[i]]=1
print(D)