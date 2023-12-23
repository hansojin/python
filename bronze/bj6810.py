#!/usr/bin/env python 

import sys
input= sys.stdin.readline

li=[9,7,8,0,9,2,1,4,1,8]
for _ in range(3):
    li.append(int(input()))

for i in range(13):
    if i%2==0:
        li[i]*=1
    else:
        li[i]*=3
print(f'The 1-3-sum is {sum(li)}')
