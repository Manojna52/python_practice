def Merge(freq1,freq2):
    return(freq1.update(freq2))
freq1={"a":2,"b":3,"c":4}
freq2={"a":4,"d":1,"b":3}
print(Merge(freq1,freq2))
print(freq1)
