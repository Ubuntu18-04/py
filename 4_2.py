l=eval(input("Enter the number that Mr. Disney has:"))
a=0
b=1
for x in range(1,l+1):
    a=a+x
    if x==l:
        print(x,end="=")
        print(a)
    else:
        print(x,end="+")
for x in range(1,l+1):
    a=a*x
    if x==l:
        print(x,end="=")
        print(a)
    else:
        print(x,end="*")
    

