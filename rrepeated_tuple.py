from collections import Counter
x=(1,2,3,4,5,3,2)
a=list(x)
freq=dict()
freq=dict(Counter(a))
for item in freq:
    if freq[item]>1:
        print(item)
    else:
        pass
