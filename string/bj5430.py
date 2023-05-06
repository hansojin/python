#!/usr/bin/env python
from collections import deque

for _ in range(int(input())):
    order=input()
    n=int(input())
    li=input()[1:-1].split(',')
    q=deque(li)
    flag=0
    if n==0:
        q=[]
    for j in order:
        if j=='R':
            flag+=1
        elif j=='D':
            if len(q)==0:
                print('error')
                break
            else:
                if flag%2==0:
                    q.popleft()
                else:
                    q.pop()
    else:
        if flag%2==1:
            q.reverse()
        print("["+",".join(q)+"]")


    
