#!/usr/bin/env python

from itertools import permutations

n=input()
li=[]
s=set()
for i in range(len(n)):
    li.append(n[i])
for i in permutations(li,len(li)):
    s.add(''.join(i))
s=sorted(list(s))

for i in range(len(s)):
    if s[i]==n:
        if i!=len(s)-1:
            print(s[i+1])
        else:
            print(0)


