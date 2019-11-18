def findcart(a1,a2,n1,n2):
    for i in range(0,n1):
        for j in range(0,n2):
            print("{" ,a1[i],",",a2[j],"}",end="")
a1=eval(input("Enter the first list"))
a2=eval(input("Enter the second list"))
n1=len(a1)
n2=len(a2)
findcart(a1,a2,n1,n2)