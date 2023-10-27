#!/usr/bin/env python

n,m=map(int,input().split())

d=[n]

def powsum(num):
    ret = 0
    sn = str(num)
    for i in range(len(sn)):
        ret+=pow(int(sn[i]),m)
    return ret
while True:
    nxt = powsum(d[-1])
    if nxt in d:
        print(d.index(nxt))
        break
    else:
        d.append(nxt)

