#!/usr/bin/env python

import math
from collections import deque

n=int(input())
if n>1:
    arr = [False,False]+[True]*(n-1)
    
    for i in range(2, int(math.sqrt(n))+1):
        if arr[i]:
            for j in range(2*i,n+1,i):
                arr[j]=False
    
    A=deque()
    A.append("B")
    for i in range(2,n+1):
        if arr[i]:
            if A[-1]=="B":
                A.pop()
                A.append("S")
                A.append("S")
            else:
                A.append("S")
                A.reverse()
        else:
            A.append("B")
    bcnt=A.count("B")
    print(bcnt,n-bcnt)


else:
    print(1,0)


