#!/usr/bin/env python

import sys
input= sys.stdin.readline

n=int(input())
li=list(map(int,input().split()))

s,e=0,n-1
ss,ee=s,e
ans=abs(li[s]+li[e])

while s<e:
    tmp = li[s]+li[e]
    if abs(tmp)<ans:
        ans=abs(tmp)
        ss,ee=s,e
        if ans==0:
            break
    if tmp<0:
        s+=1
    else:
        e-=1
print(li[ss],li[ee])
        

