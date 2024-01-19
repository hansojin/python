#!/usr/bin/env python

import sys
input= sys.stdin.readline

ans=[]
for _ in range(int(input())):
    a,b,c,d=sorted(list(map(int,input().split())))
    if a==b==c==d:
        ans.append(50000+a*5000)
    elif a!=b and b==c==d:
        ans.append(10000+b*1000)
    elif a==b==c and c!=d:
        ans.append(10000+a*1000)
    elif a==b and c==d and b!=c:
        ans.append(2000+a*500+c*500)
    elif a==b and b!=c and c!=d:
        ans.append(1000+a*100)
    elif a!=b and b==c and c!=d:
        ans.append(1000+b*100)
    elif a!=b and b!=c and c==d:
        ans.append(1000+c*100)
    else:
        ans.append(d*100)
print(max(ans))
    
