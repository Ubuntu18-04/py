out=open("leaders.txt",'w')
out.writelines("Leaders are:\nline no:\tCode snippet:\n")
with open("8.py",'r')as IP:
    for j,i in enumerate(IP,1):
        if i.strip().endswith(":"):
            out.writelines(str(j)+"\t"+i.strip()[:-1]+"\n")
out.close()
out=open("Functions.txt",'w')
out.writelines("Functions are:\nline no\tCode snippet:\n")
with open("8.py",'r')as IP:
    for i,j in enumerate(IP,1):
        if j.strip().startswith("def"):
            out.writelines(str(i)+"\t"+j.strip()[:-1]+"\n")
out.close