#!/usr/bin/env python

import sys
input = sys.stdin.readline

n=int(input())
li=[]
for _ in range(n):
    word=input().rstrip()
    li.append(word)

li.sort()   
li.sort(key=lambda x : len(x))

ans=[]
for i in range(n):
    if li[i] not in ans:
        ans.append(li[i])
        print(li[i])

