import math as m
ls=[]
mean=med=0 
sum=0
n=int(input("Enter the number of elements in the list:"))
for i in range(0,n):
    ele=int(input())
    mean+=ele
    ls.append(ele)
mean/=n
for i in ls:
    sum+=((i-mean)**2)
sd=m.sqrt(sum/n)
#mode
ls.sort()
if n%2==0:
    med=((ls[int(n/2)])+(ls[int((n/2))-1]))/2
else:
    med=ls[(n//2)]
print(ls," Mean= ",mean, "Standard deviation=",sd,"Median=",med)

c=[]
for i in range(0,n-1):
    c[i]=1
for i in range(0,n-1):
    if ls[i]==ls[i+1]:
        c[i]=c[i]+1
print(c)