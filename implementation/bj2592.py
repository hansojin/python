#!/usr/bin/env python

from collections import Counter

li=[]
for _ in range(10):
    li.append(int(input()))
print(sum(li)//10)
app = Counter(li).most_common()
print(app[0][0])


