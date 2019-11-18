a={}
n=eval(input("Enter the number of inputs"))
no,p,c,m,b=[],[],[],[]
for i in range(n):
    no.append(input("Enter the serial numbers in order"))
for i in range(n):
    p.append(input("Enter the physics numbers in order"))
for i in range(n):
    c.append(input("Enter the chem numbers in order"))
for i in range(n):
    m.append(input("Enter the math numbers in order"))
for i in range(n):
    b.append(input("Enter the bio numbers in order"))
for i in range(n):
    a[no[i]]=[p[i],c[i],m[i],b[i]]
for i in a:
    print(i,"==>",end=" ")
    for j in a[i]:
        print(j,end=" ")
print()

tot={}
for i in a:
    tot[i]=sum(a[i])
for i,j in sorted(tot.items(),key**lambda,a:a[l]):
    print(i,"==>",j)

details={}
