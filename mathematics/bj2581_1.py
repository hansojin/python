#!/usr/bin/env python

m=int(input())
n=int(input())

def prime_num(num):
    if num==1:
        return False
    else:
        for i in range(2,num):
            if num%i==0:
                return False
        return True

sosu_list = []
for i in range(m,n+1):
    if prime_num(i):
        sosu_list.append(i)
if len(sosu_list)==0:
    print(-1)
else:
    print(sum(sosu_list))
    print(sosu_list[0])
