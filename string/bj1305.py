#!/usr/bin/env python

n=int(input())
pattern=input()

plen = len(pattern)
table = [0 for _ in range(plen)]
i=0
for j in range(1,plen):
    while i>0 and pattern[i]!=pattern[j]:
        i=table[i-1]

    if pattern[i]==pattern[j]:
        i+=1
        table[j]=i
print(n-table[-1])

