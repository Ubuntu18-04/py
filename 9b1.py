print("union")
with open("a.txt")as f1,open("b.txt") as f2:
     for i,j in zip(f1,f2):
        if(set(i.split())==set(j.split())):
            print(i.strip())
        else:
         print(i.strip(),j.strip()) 

print("intersection")
with open("a.txt")as f1,open("b.txt")as f2:
    for i,j in zip(f1,f2):
        if set(i.split())==set(j.split()):
            print(i.split())

print("f1-f2")
with open("a.txt")as f1,open("b.txt")as f2:
    for i,j in zip(f1,f2):
        if set(i.split())==set(j.split()):
            pass
        else:
            print(i.strip())

print("symmetric difference")
with open("a.txt")as f1,open("b.txt"):
    for i,j in zip(f1,f2):
        if set(i.split())==set(j.split()):
            pass
        else:
          print(i.split(),j.split())