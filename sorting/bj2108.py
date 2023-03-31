#!/usr/bin/env python

import sys
input = sys.stdin.readline
from collections import Counter

n=int(input())
li=[]
for _ in range(n):
    li.append(int(input()))

li.sort()

print(round(sum(li)/n))
print(li[n//2])

cnt=Counter(li).most_common(2)  #빈도수 높은 두개 가져오기
if len(li)>1:
    if cnt[0][1]==cnt[1][1]:
        print(cnt[1][0])
    else:
        print(cnt[0][0])
else:
    print(cnt[0][0])

print(li[-1]-li[0])
