from collections import Counter
a=(1,2,3,4,6,8)
x=dict()
t=[]
t=list(a)
x=dict(Counter(t))
print(x)

