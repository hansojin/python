#!/usr/bin/env python
import sys
input=sys.stdin.readline

n=int(input())
stack=[]

for i in range(n):
    ask=input().split()
    
    if ask[0]=="push":
        stack.append(ask[1])
    elif ask[0]=="pop":
        if len(stack)==0:
            print(-1)
        else:
            print(stack.pop())
    elif ask[0]=="size":
        print(len(stack))
    elif ask[0]=="empty":
        if len(stack)==0:
            print(1)
        else:
            print(0)
    elif ask[0]=="top":
        if len(stack)==0:
            print(-1)
        else:
            print(stack[-1])



