#!/usr/bin/env python

import sys
input = sys.stdin.readline

def cal(arr,length):
    global ans
    if arr:
        i = 0
        while i < length - 1:
            ans += max(arr[i] * arr[i + 1], arr[i] + arr[i + 1])
            i += 2
        if length % 2 == 1:
            ans += arr[length - 1]

n=int(input())
ans=0
li,po,ne=[],[],[]

for _ in range(n):
    li.append(int(input()))
cnt=0
for i in li:
    if i>0:
        po.append(i)
    if i<0:
        ne.append(i)
    if i==0:
        cnt+=1
po.sort(reverse=True)
ne.sort()
for _ in range(cnt):
    ne.append(0)

pol,nel=len(po),len(ne)

cal(po,pol)
cal(ne,nel)

print(ans)
