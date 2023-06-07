#!/usr/bin/env python

import sys
input= sys.stdin.readline

dic={chr(i):0 for i in range(97,123)}
for _ in range(int(input())):
    name=str(input())
    dic[name[0]]+=1

ans=""
for key,val in dic.items():
    if val>=5:
        ans+=key
if ans:
    print(ans)
else:
    print("PREDAJA")


