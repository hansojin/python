#!/usr/bin/env python

import sys
input= sys.stdin.readline

def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)

for i in range(int(input())):
    li=[]
    a=list(map(int,input().split()))
    al=len(a)
    for j in range(al):  
        for k in range(al):  
            if j>k and j!=k:
                li.append(gcd(a[j],a[k]))  
            else:
                pass
    print(max(li))
