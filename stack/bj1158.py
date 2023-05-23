#!/usr/bin/env python

n,k=map(int,input().split())
li=[i for i in range(1,n+1)]
ans=[]
cnt=0

for i in range(n):
    cnt+=k-1
    if cnt>=len(li):
        cnt=cnt%len(li)
    ans.append(str(li.pop(cnt)))
print('<', ', '.join(ans), '>', sep='')
