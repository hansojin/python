#!/usr/bin/env python
from collections import deque
q=deque()
n=int(input())
for i in range(1,n+1):
    q.append(i)


while q:
    print(q.popleft(),end=' ')
    q.rotate(-1)
