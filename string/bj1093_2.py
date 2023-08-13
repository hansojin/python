#!/usr/bin/env python

from itertools import product

a,b=map(str,input().split())
c,d=map(str,input().split())
li=[a,b,c,d]
res = list(product(li,repeat=2))
res=list(set(res))
res=sorted(res, key = lambda x : (x[0],x[1]))
for i in res:
    print(i[0],i[1])
