#!/usr/bin/env python
import sys
input = sys.stdin.readline

q=[]

for i in range(int(input())):
    order=input().split()
    if order[0]=='push':
        q.append(order[1])

    elif order[0]=='pop':
        if q:
            print(q.pop(0))
        else:
            print(-1)

    elif order[0]=='size':
        print(len(q))

    elif order[0]=='empty':
        if q:
            print(0)
        else:
            print(1)

    elif order[0]=='front':
        if q:
            print(q[0])
        else:
            print(-1)
    else:
        if q:
            print(q[-1])
        else:
            print(-1)
