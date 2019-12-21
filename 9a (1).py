f1=open("a.txt","r")
f2=open("b.txt",'w')
k=1
for lines in f1:
    f2.write(str(k))
    f2.write(lines)
    k=k+1
f1.close()
f2.close()
