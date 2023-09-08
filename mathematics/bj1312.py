#!/usr/bin/env python
a,b,c= map(int,input().split())

for i in range(c):
    a=(a%b)*10
    ans=a//b
print(ans)
