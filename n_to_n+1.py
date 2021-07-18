x=input().split(' ')
x.insert(0,0)
x[0]=x[len(x)-1]
x.pop()
print(x)
