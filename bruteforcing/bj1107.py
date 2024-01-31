#!/usr/bin/env python

import sys
input= sys.stdin.readline

ch=int(input())
ans=abs(100-ch)
m=int(input())
if m:
    br=set(input().split())
else:
    br=set()

for num in range(1000001):
    for n in str(num):
        if n in br:
            break
    else:
        ans=min(ans,len(str(num))+abs(num-ch))
print(ans)
