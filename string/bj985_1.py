#!/usr/bin/env python

import sys
input = sys.stdin.readline

n=int(input())
li=list(map(int,input().split()))
ans=[]

for i in li:
    if i<250:
        ans.append(4)
    elif 250<=i<275:
        ans.append(3)
    elif 275<=i<300:
        ans.append(2)
    else:
        ans.append(1)

print(*ans)
