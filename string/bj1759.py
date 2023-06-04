#!/usr/bin/env python

import sys
input= sys.stdin.readline
from itertools import combinations

def code():
    res=[]
    for c in list(combinations(li,n)):
        vol,cnt=0,0
        for char in c:
            if char in vowels:
                vol+=1
            else:
                cnt+=1
        if vol>0 and cnt>1:
            res.append(''.join(c))
    return res

n,m=map(int,input().split())
li=list(map(str,input().split()))
li=sorted(li)
vowels=set(['a','e','i','o','u'])

for i in code():
    print(i)
