#!/usr/bin/env python

import sys
input= sys.stdin.readline

li=[]
while True:
    num=list(map(int,input().split()))
    if len(num)==0:
        break
    li.append(num)
del li[0][0]
ans=[]
for nums in li:
    for i in nums:
        n=int(str(i)[::-1])
        ans.append(n)
ans.sort()

for i in ans:
    print(i)

