#!/usr/bin/env python

import sys
input= sys.stdin.readline

n,m=map(int,input().split())

now,ans=1,0
apple=[]

for _ in range(int(input())):
    apple.append(int(input()))
for a in apple:
    if now<=a and now+(m-1)>=a:
        pass
    elif now>a:
        ans+=abs(a-now)
        now=a
    else:
        ans+=a-(m-1)-now
        now=a-(m-1)
print(ans)
