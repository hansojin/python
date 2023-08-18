#!/usr/bin/env python

x = int(input())
arr = list(map(int, input().split()))

dp = [1 for i in range(x)]

for i in range(x):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)

max_dp = max(dp)
print(max_dp)

max_idx = dp.index(max_dp)
li = []

while max_idx >= 0:
    if dp[max_idx] == max_dp:
        li.append(arr[max_idx])
        max_dp -= 1
    max_idx -= 1

li.reverse()
print(*li)
