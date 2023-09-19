#!/usr/bin/env python

import math
from itertools import permutations

while True:
    try:
        n,m=input().split()
        maxx= math.factorial(len(n))
        if int(m)>maxx:
            print(f'{n} {m} = No permutation')
        else:
            li=sorted(list(n))
            cnt=0
            for i in permutations(li,len(li)):
                cnt+=1
        
                if cnt==int(m):
                    ans=''.join(i)
                    break
            print(f'{n} {m} = {ans}')
    except:
        break

