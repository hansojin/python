#!/usr/bin/env python

from collections import deque
import sys
input = sys.stdin.readline

q=deque()

for _ in range(int(input())):
    order = input().split()
    if order[0] == "push_front":
        q.appendleft(order[1])
    elif order[0]=="push_back":
        q.append(order[1])
    elif order[0]=="pop_front":
        if len(q)==0:
            print(-1)
        else:
            print(q.popleft())
    elif order[0]=="pop_back":
        if len(q)==0:
            print(-1)
        else:
            print(q.pop())
    elif order[0]=="size":
        print(len(q))
    elif order[0]=="empty":
        if len(q)==0:
            print(1)
        else:
            print(0)
    elif order[0]=="front":
        if len(q)==0:
            print(-1)
        else:
            print(q[0])
    elif order[0]=="back":
        if len(q)==0:
            print(-1)
        else:
            print(q[-1])


'''
큐가 빈거 확인할 때 len을 써도 되는데,

if q:   #존재할때.로도 쓸수 있음
    print(q[0])
else:
    print(-1)




'''

