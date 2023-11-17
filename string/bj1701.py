#!/usr/bin/env python

pattern=input()

plen = len(pattern)

def kmp(pattern):
    plen=len(pattern)
    table = [0 for _ in range(plen)]
    i=0
    for j in range(1,plen):
        while i>0 and pattern[i]!=pattern[j]:
            i=table[i-1]

        if pattern[i]==pattern[j]:
            i+=1
            table[j]=i
    return table

ans=0
for i in range(plen):
    ans=max(ans,max(kmp(pattern[i:])))

print(ans)
