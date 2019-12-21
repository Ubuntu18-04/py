out=open('leaders.txt','w')
out.writelines("leaders are:\n line no\t code snippet\n")

with open("input.py","r")as IP:
    for j,i in enumerate(IP,1):
        if i.strip().endswith(":"):
              out.writelines(str(j)+"\t"+  i.strip()[:-1]+"\n")
out.close()

out=open("function.txt","w")
out.writelines("functions are:\nlines no\tcode snippet\n")

with open("input.py","r")as IP:
    for i,j in enumerate(IP,1):
        if j.strip().startswith("def"):
            out.writelines(str(i)+'\t'+j.strip()[:-1]+'\n')
out.close()