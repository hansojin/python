#!/usr/bin/env python

n = int(input())
for _ in range(n):
    s, w = map(str, input().split())
    cnt = 0
    cnt = s.count(w)
    replaced_s = s.replace(w, "")
    print(cnt + len(replaced_s))
