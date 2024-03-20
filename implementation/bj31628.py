#!/usr/bin/env python

import sys
input= sys.stdin.readline

li=[list(input().split()) for _ in range(10)]

flag=False

for v in li:
    if len(set(v))==1:
        flag=True
        break

for j in range(10):
    st=set()
    for i in range(10):
        st.add(li[i][j])

    if len(st)==1:
        flag=True
        break
if flag:
    print(1)
else:
    print(0)
