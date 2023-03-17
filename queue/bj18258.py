#!/usr/bin/env python

import sys
input = sys.stdin.readline
q=[]
cnt=0
for _ in range(int(input())):
    order=input().split()

    if order[0]=='push':
        q.append(order[1])
    elif order[0]=='pop':
        if len(q)-cnt==0:
            print(-1)
        else:
            print(q[cnt])
            cnt+=1
            #q.pop(0)   _ pop 대신 cnt를 ++ 해서 그대로 읽는 방향으로
    elif order[0]=='size':
        print(len(q)-cnt)
    elif order[0]=='empty':
        if len(q)-cnt ==0:
            print(1)
        else:
            print(0)
    elif order[0]=='front':
        if len(q)-cnt ==0:
            print(-1)
        else:
            print(q[cnt])
    else:
        if len(q)-cnt==0:
            print(-1)
        else:
            print(q[-1])

