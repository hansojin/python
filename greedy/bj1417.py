#!/usr/bin/env python

vote=[]
n=int(input())
ds=int(input())
for _ in range(n-1):
    votes=int(input())
    vote.append(votes)
vote.sort(reverse=True)

cnt=0
if n==1:
    print(0)

else:
    while ds<=vote[0]:
        ds+=1
        vote[0]-=1
        cnt+=1
        vote.sort(reverse=True)
    print(cnt)
