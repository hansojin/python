#!/usr/bin/env python

import math

n = int(input())
cnt=0
array = [True for i in range(n + 1)] 

for i in range(2, int(math.sqrt(n)) + 1): 
    if array[i] == True: 
        j = 2
        while i * j <= n:
            array[i * j] = False
            j += 1
prime=[]
for i in range(2, n + 1):
    if array[i]:
        prime.append(i)

cnt,summ=0,0
s,e=0,0

while True:
    if summ==n:
        cnt+=1

    if summ>n:
        summ-=prime[s]
        s+=1
    elif e==len(prime):
        break
    else:
        summ+=prime[e]
        e+=1
print(cnt)
