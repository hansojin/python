#!/usr/bin/env python

n=int(input())
for _ in range(n):
    ps=input()
    li=list(map(str,str(ps)))
    cnt=0
    for i in range(len(li)):
        if li[i]=='(':
            cnt+=1
        else:
            cnt-=1
    if cnt==0:
        print("YES")
    else:
        print("NO")

