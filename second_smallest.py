x=input().split(' ')
freq=dict()
for i in range(0,len(x)):
    x[i]=int(x[i])
    if x[i] in freq:
        freq[x[i]]+=1
    else:
        freq[x[i]]=0
a=[]
for item in freq:
    a.append(item)
a.sort()
print(a[1])
