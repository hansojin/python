#!/usr/bin/env python

n = int(input())
arr = input().split()

p1_m,p1_j = n,0 
p2_m,p2_j = n,0 
p2_arr = []

arr = list(map(int,arr))

for cost in arr:
    p1_j += p1_m//cost 
    p1_m = p1_m%cost 
    
    p2_arr.append(cost)
    if len(p2_arr) >= 4: 
        if p2_arr[0] > p2_arr[1] > p2_arr[2]: 
            p2_j += p2_m//cost 
            p2_m = p2_m%cost
        elif p2_arr[0] < p2_arr[1] < p2_arr[2]: 
            p2_m += p2_j*cost 
            p2_j = 0 
        p2_arr.pop(0)

if p1_m + arr[-1]*p1_j > p2_m + arr[-1]*p2_j:
    print('BNP')
elif p1_m + arr[-1]*p1_j < p2_m + arr[-1]*p2_j:
    print('TIMING')
else:
    print('SAMESAME')
