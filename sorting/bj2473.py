#!/usr/bin/env python

import sys
input= sys.stdin.readline

n=int(input())
li=sorted(list(map(int,input().split())))
minn = sys.maxsize
sol=[]

for i in range(n-2):
    if i>0 and li[i]==li[i-1]:
        continue
    lp = i+1
    rp = n-1

    while lp<rp:
        summ = li[i] + li[lp] + li[rp]
        diff = abs(summ)

        if diff<minn:
            minn=diff
            sol=[i,lp,rp]

        if summ<0:
            lp+=1
        elif summ>0:
            rp-=1
        else:
            break
    if not minn:
        break

print(li[sol[0]], li[sol[1]], li[sol[2]])
