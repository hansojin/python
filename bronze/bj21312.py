#!/usr/bin/env python

li=list(map(int,input().split()))
even,odd=[],[]
for i in li:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
ans=1
if odd:
    for i in odd:
        ans*=i
else:
    for i in even:
        ans*=i
print(ans)

