#!/usr/bin/env python

li=[0]*81
A,B,C=map(int,input().split())
for a in range(1,A+1):
    for b in range(1,B+1):
        for c in range(1,C+1):
            li[a+b+c]+=1
print(li.index(max(li)))

