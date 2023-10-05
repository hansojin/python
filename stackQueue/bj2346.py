#!/usr/bin/env python

from collections import deque

n=int(input())
q=deque(enumerate(map(int,input().split())))
ans=[]
while q:
    idx,pp = q.popleft()
    ans.append(idx+1)

    if pp>0:
        q.rotate(-(pp-1))
    elif pp<0:
        q.rotate(-pp)
print(' '.join(map(str,ans)))
