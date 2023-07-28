#!/usr/bin/env python

import sys
input= sys.stdin.readline

def my_round(n):
    if n-int(n)>=0.5:
        return int(n)+1
    else:
        return int(n)

n=int(input())
if n==0:
    ans=0

else:
    li=[]
    for i in range(n):
        li.append(int(input()))
    li.sort()
    out = my_round(n*0.15)

    ans=my_round(sum(li[out:n-out])/(n-(2*out)))

print(ans)
