#!/usr/bin/env python

n=int(input())
li=[]
for _ in range(n):
    li.append(int(input()))
li.sort()
ans=[]

for j in range(2,li[0]+1):
    for i in range(1,n):
        res=li[0]%j
        if li[i]%j!=res:
            break
        ans.append(j)
ans=set(ans)
print(*ans)
