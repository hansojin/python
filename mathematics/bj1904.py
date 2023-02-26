#!/usr/bin/env python

import math
fac = math.factorial
n=int(input())
cnt=0
for a in range(n//2+1):
    b=n-2*a
    cnt+=fac(a+b)//(fac(a)*fac(b))
print(cnt)
