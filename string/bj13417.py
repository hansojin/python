#!/usr/bin/env python
from collections import deque

for _ in range(int(input())):
    n=int(input())
    tmp=list(map(str,input().split()))
    ans=[tmp[0]]

    ans=deque(ans)
    for i in range(1,len(tmp)):
        if tmp[i] > ans[0]:
            ans.append(tmp[i])
        else:
            ans.appendleft(tmp[i])
    res="".join(ans)
    print(res)
    

    

