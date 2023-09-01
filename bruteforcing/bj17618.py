#!/usr/bin/env python

cnt=1

n=int(input())

def add(n):
    stn= list(map(int,str(n)))
    return sum(stn)

for i in range(2,n+1):
    if i%add(i)==0:
        cnt+=1
print(cnt)

# instead of add Function
# sum([int(c) for c in str(i)] is also possbile
