#!/usr/bin/env python

n, m = map(int, input().split())

ans = m - n + 1
li = [False] * (m-n+1)

for i in range(2, int(m**0.5+1)):
    s = i**2
    for j in range((((n-1)//s)+1)*s, m+1, s):
        if not li[j-n] :
            li[j-n] = True
            ans -= 1
print(ans)

