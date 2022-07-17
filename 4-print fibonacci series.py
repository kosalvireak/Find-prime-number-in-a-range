n = 300
i =0
m = 1
o = i + m
while o<n:
    o = i + m
    m = m + o
    print(i,m,o)
    i = m
    