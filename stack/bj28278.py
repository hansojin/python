#!/usr/bin/env python

import sys
input= sys.stdin.readline

stack = []
for _ in range(int(input())):
    i = input()
    op = int(i[0])
    if op==1:
        stack.append(int(i[2:]))
    elif op==2:
        if len(stack)==0:
            print(-1)
        else:
            print(stack.pop())
    elif op==3:
        print(len(stack))
    elif op==4:
        if len(stack)>0:
            print(0)
        else:
            print(1)
    elif op==5:
        if len(stack)>0:
            print(stack[-1])
        else:
            print(-1)
