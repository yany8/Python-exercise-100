"""for i in range(1,1001):
    s = 0
    L = []
    for x in range(1,int((i+3)/2)):
        if i % x == 0:
            s += x
            L.append(x)
    if i == s:
         print(i)
         print(L)"""
s = []
for i in range(1,1001):
    sum = 1
    for j in range(1, i):
        if i % j == 0:
            sum += j
            if j not in s and j != 1:
                s.append(j)
    if sum == i:
        print(j)
        print(s)
"""        
from sys import stdout
for j in range(2,1001):
    k = []
    n = -1
    s = j
    for i in range(1,j):
            if j % i == 0:
                n += 1
                s -= i
                k.append(i)
    
    if s == 0:
        print(j)
        for i in range(n):
            stdout.write(str(k[i]))
            stdout.write(' ')
        print(k[n])
"""
