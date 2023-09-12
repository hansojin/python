#!/usr/bin/env python

import sys
input= sys.stdin.readline

n,m=map(int,input().split())
x,y=map(int,input().split())
rem,am = 0,0
ans=1
for _ in range(m):
    a,b=map(int,input().split())
    if a==0:
        am+=1
    else:
        rem+=1

tmp=n-rem
if tmp>0:
    for i in range(tmp,tmp-am,-1):
        ans*=i

tp = tmp-am
if tp>0:
    for i in range(9-m, 9-m-tp,-1):
        ans*=i
if ans%3==0:
    delay = ans//3 -1
    if delay<0:
        delay=0
else:
    delay = ans//3
ans*=x
ans+=delay*y
print(ans)


