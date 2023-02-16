#!/usr/bin/env python

li=[]
ans=0
for _ in range(9):
    hght=int(input())
    li.append(hght)
    ans+=hght

ans-=100
non=[]
for i in range(0,8):
    for j in range(i+1,9):
            
            if li[i]+li[j]==ans:
                non.append(i)
                non.append(j)
                break

del(li[non[0]])
del(li[non[1]-1])
li.sort()
for i in range(7):
    print(li[i])
