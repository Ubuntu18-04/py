def mod(d):
    res={}
    for i in d:
        if d[i] not in res:
            res[d[i]]=[]
            res[d[i]].append(i)
        else:
            res[d[i]].append(i)
    return res
X={'apple':'fruit','cat':'mammal','beans':'veg','dog':'mammal','mango':'fruit','brinjal':'veg','potato':'veg','horse':'mammal'}
print(mod(X))