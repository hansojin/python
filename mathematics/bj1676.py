#!/usr/bin/env python

import math
n=int(input())

num=math.factorial(n)
li=[]
for i in map(int,str(num)):
    li.append(i)

cnt=0
for i in reversed(li):
    if i==0:
        cnt+=1
    else:
        print(cnt)
        break
