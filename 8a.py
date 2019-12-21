def mylist(l1=[],l2=[]):
    k=max(l1)
    for a,b in zip(l1,l2):
        if a==k:
            print(a,b)
#mylist([90,80,75,95],['a','b','c','d'])
def enter(l,n,text=False):
    print("Enter the elements:")
    for i in range(n):
        if(text):
            l.append(input())
        else:
            l.append(int(input()))
            

marks,names=[],[]            
n1=int(input("Enter the number of mark: "))
enter(marks,n1)
n2=int(input("Enter the number of names: "))
enter(names,n2,True)
print(marks,names,sep="\n")
print(mylist(marks,names))

