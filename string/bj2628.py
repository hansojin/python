#!/usr/bin/env python

n,m=map(int,input().split())
mLi=[0 for _ in range(m+1)]
nLi=[0 for _ in range(n+1)]
mLi[0],mLi[m],nLi[0],nLi[n]=1,1,1,1

for i in range(int(input())):
    a,b=map(int,input().split())
    if a==0:
        mLi[b]=1
    else:
        nLi[b]=1

mtmp,ntmp=[],[]
for i in range(len(mLi)):
    if mLi[i]==1:
        mtmp.append(i)
for i in range(len(nLi)):
    if nLi[i]==1:
        ntmp.append(i)
mmax,nmax=0,0
for i in range(len(mtmp)-1):
    tmp=abs(mtmp[i+1]-mtmp[i])
    if mmax<tmp:
        mmax=tmp

for i in range(len(ntmp)-1):
    tmp=abs(ntmp[i+1]-ntmp[i])
    if nmax<tmp:
        nmax=tmp
print(nmax*mmax)

