#!/usr/bin/env python

N = int(input())
data = list(map(int, input().split()))

height = data[0]
rslt = []
cnt = 0

for i in range(1,N):
    if height > data[i]:
        cnt += 1
    else:
        height = data[i]
        cnt = 0
    rslt.append(cnt)

print(max(rslt))
