a = range(10)
b=[el*2 for el in a ]
print(b)

L=[1,2]
L2=["a","b"]
L3=[4,5]

f=[(e1,e2,e3) for e3 in L3 for e2 in L2 for e1 in L]

print()