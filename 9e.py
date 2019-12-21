import mystat as ms 
l=[]
n=int(input("enter no. of items"))
for i in range(0,n):
    
    i=int(input("enter numbers"))
    l.append(i)
print(l)
print("sum of the list",sum(l))
print("average",ms.avg(l,n))
print("SD",ms.stand(l,n))