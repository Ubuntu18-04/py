marks,names=[],[]
n=int(input("Enter the no of students: "))
for i in range(0,n):
    marks.append(int(input("enter marks: ")))
    names.append(str(input("enter names: ")))
def maximum(ma,na):
    maxmarks=max(ma)
    i=ma.index(maxmarks)
    name=na[i]
    return(maxmarks,name)    
maxi=maximum(marks,names)
print("marks: ",marks)
print("names: ",names)
print(maxi)