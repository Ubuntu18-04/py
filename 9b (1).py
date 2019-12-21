import sys
c=input("1.union\n2:intersection\n3:file1-file2\n4:file2-file1\n")
f1=open("a.txt","r")
f2=open("bc.txt","r")
f3=open("9b.txt","w+")
b=0
if c=="1":
      for lines in f1:
          f3.write(lines)
      for lines in f2:
          f3.write(lines)
elif c=="2":
      for lines in f1:
            for line in f2:
                   if line==lines:
                         f3.write(lines)
            f2.seek(0)
elif c=="3":
       for lines in f1:
            for line in f2:
                 if line==lines:
                    b=1;
                    break;
            if b==0:
                    f3.write(lines)
            f2.seek(0)
