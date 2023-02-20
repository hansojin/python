#!/usr/bin/env python

n=int(input())
nums=[]
for _ in range(n):
    nums.append(int(input()))

nums.sort(reverse=True)
ans=[]
for i in range(n):
    ans.append(nums[i]*(i+1))
print(max(ans))
