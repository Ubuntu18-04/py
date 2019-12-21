A={}
S,p_marks,c_marks,m_marks,b_marks=[],[],[],[],[]
n=int(input("enter the number of records"))
for i in range(n):
    S.append(input("enter srn"))
for i in range(n):
    p_marks.append(int(input("enter marks  in physics")))
for i in range(n):
    c_marks.append(int(input("enter C marks")))
for i in range(n):
    m_marks.append(int(input("enter m marks")))
for i in range(n):
    b_marks.append(int(input("enter b marks")))
for i in range(n):
    A[S[i]]=[p_marks[i],c_marks[i],m_marks[i],b_marks[i]]

for i in A:
    print(i,"==>",end=" ")
    for j in A[i]:
        print(j,end=' ')
print()

Total={}
for i in A:
    Total[i]=sum(A[i])
for i,j in sorted(Total.items(),key=lambda a: a[1]):
    print(i,"==>",j)

student_details={}
for i in m_marks:
    student_details[i]=[] 
    for j in A:
        if(i==A[j][2]):
            student_details[i].append(j)
print(student_details)