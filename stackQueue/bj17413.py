#!/usr/bin/env python

p=input()
stack=[]
res=''
tag=False

for s in p:
    if s==' ':
        while stack:
            res+=stack.pop()
        res+=s
    elif s=='<':
        while stack:
            res+=stack.pop()
        tag=True
        res+=s
    elif s=='>':
        tag=False
        res+=s
    elif tag:
        res+=s
    else:
        stack.append(s)
while stack:
    res+=stack.pop()
print(res)
