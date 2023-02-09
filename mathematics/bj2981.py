#!/usr/bin/env python

import math
n=int(input())
li=[]
gcd =0

for i in range(n):
    li.append(int(input()))
    if i==1:
        gcd=abs(li[1]-li[0])
    gcd=math.gcd(abs(li[i]-li[i-1]),gcd)

ra=int(gcd**0.5)
ans=[]

for i in range(2,ra+1):
    if gcd%i==0:
        ans.append(i)
        ans.append(gcd//i)
    ans.append(gcd)
ans.append(gcd)
ans=list(set(ans))
ans.sort()
print(*ans)
