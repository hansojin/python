#!/usr/bin/env python

import sys
input = sys.stdin.readline

n=int(input())
word=[]

for i in range(n):
    word.append(input().rstrip())

li=list(set(word))
li.sort()
li.sort(key=len)

for i in range(len(li)):
    print(li[i])
