#!/usr/bin/env python

import sys
input=sys.stdin.readline

n,m=map(int,input().split())

a=list(map(int,input().split()))
b=list(map(int,input().split()))

i=0
j=0
ans = []
while True:

    if a[i]<=b[j]:
        ans.append(a[i])
        i+=1
    else:
        ans.append(b[j])
        j+=1

    if i==n or j==m:
        ans+= a[i:] + b[j:]
        break
print(*ans)

