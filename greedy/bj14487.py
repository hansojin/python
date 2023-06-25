#!/usr/bin/env python

n=input()
li=list(map(int,input().split()))
ans=sum(li)
li.sort()
print(ans-li[-1])
