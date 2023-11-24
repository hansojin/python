#!/usr/bin/env python

import sys
input= sys.stdin.readline

n=int(input())
li=sorted((list(map(int, input().split())) for _ in range(n)))
leng = li[0][1]-li[0][0]
target = li[0][1]

for i in range(1,len(li)):
    if li[i][0]<target<li[i][1] or li[i][0]==target:
        leng+=li[i][1]-target
        target=li[i][1]
    elif li[i][0]>target:
        leng+=li[i][1]-li[i][0]
        target=li[i][1]
print(leng)
