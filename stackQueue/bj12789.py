#!/usr/bin/env python

import sys
input= sys.stdin.readline

n=int(input())
li=list(map(int,input().split()))

num=1
stack=[]

for i in li:
    stack.append(i)
    while stack and stack[-1]==num:
        stack.pop()
        num+=1
    if len(stack)>1 and stack[-1]>stack[-2]:
        print('Sad')
        sys.exit()
if stack:
    print('Sad')
else:
    print('Nice')
