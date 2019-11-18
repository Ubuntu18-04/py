print("UNION")
with open("Q2_test.txt")as f,open("Q2_out.txt")as f1:
    for i,j in zip(f,f1):
        if set(i.split())==set(j.split()):
            print(i.strip())
        else:
            print(i.strip())
            print(j.strip())
print("INTERSECTION")
with open("Q2_test.txt") as f,open("Q2_out.txt")as f1:
    for i,j in zip(f,f1):
        if set(i.split())==set(j.split()):
            print(i.strip())
print("SET1-SET2")
with open("Q2_test.txt") as f,open("Q2_out.txt")as f1:
    for i,j in zip(f,f1):
        if set(i.split())==set(j.split()):
            pass
        else:
            print(i.strip())
print("SYMMETRIC DIFFERENCE")
with open("Q2_test.txt")as f,open("Q2_out.txt")as f1:
    for i,j in zip(f,f1):
        if set(i.split())==set(j.split()):
            pass
        else:
            print(i.strip())
            print(j.strip())