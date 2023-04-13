#!/usr/bin/env python

import sys
input = sys.stdin.readline

num=[]
for i in range(8):
    num.append([int(input()),i+1])

num.sort(key = lambda x: -x[0])
ans=0
li=[]
for i in range(0,5):
    ans+=num[i][0]
    li.append(num[i][1])

print(ans)
li.sort()
print(*li)

