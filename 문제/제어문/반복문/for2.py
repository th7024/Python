num = int(input())
L = list(range(2, num+1))
for i in L:
    for j in L:
        if i!=j and j%i==0 :
            L.remove(j)
print(L)