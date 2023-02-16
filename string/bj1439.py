#!/usr/bin/env python
import math
num=str(input())
cnt=0
for i in range(len(num)-1):
    if num[i]!=num[i+1]:
        cnt+=1

print(math.ceil(cnt/2))
