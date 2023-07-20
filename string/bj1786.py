#!/usr/bin/env python

import sys
input= sys.stdin.readline

t=str(input()).rstrip()
p=str(input()).rstrip()
pLen=len(p)-1
t=t.replace(p,'*')
arr,ans=[],[]
for i in range(len(t)):
    if t[i]=='*':
        arr.append(i)
print(len(arr))
cnt=0
for i in arr:
    ans.append(i+cnt*pLen+1)
    cnt+=1
print(*ans)
