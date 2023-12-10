#!/usr/bin/env python

n = int(input())
li = list(map(int, input().split()))
ans = 0
ir = 1
for i in range(0, n-3):
    ir *= li[i]
    jr = 1
    for j in range(i+1, n-2):
        jr *= li[j]
        kr = 1
        for k in range(j+1, n-1):
            kr *= li[k]
            lr = 1
            for l in range(k+1, n):
                lr *= li[l]
            ans = max(ans, ir+jr+kr+lr)
print(ans)
