#!/usr/bin/env python

n= int(input())
for i in range(n):
    rank = int(input())
    if rank<=25:
        print(f'Case #{i+1}: World Finals')
    elif rank<=1000:
        print(f'Case #{i+1}: Round 3')
    elif rank<=4500:
        print(f'Case #{i+1}: Round 2')
    else:
        print(f'Case #{i+1}: Round 1')
        
