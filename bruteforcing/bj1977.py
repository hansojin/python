#!/usr/bin/env python

import math
m=math.ceil(math.sqrt(int(input())))
n=math.floor(math.sqrt(int(input())))
sum=0
if m<n:
    for i in range(m,n+1):
        sum+=i*i
    print(sum)
    print(m*m)
else:
    print(-1)
