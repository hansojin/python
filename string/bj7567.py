#!/usr/bin/env python

n=input()
lgth=len(n)
ans=lgth*10

for i in range(1,lgth):
    if n[i]==n[i-1]:
        ans-=5
print(ans)
