#!/usr/bin/env python

import sys
input= sys.stdin.readline

n=input().rstrip()
n=n.replace("apa","a").replace("epe","e").replace("ipi","i").replace("opo","o").replace("upu","u")
print(n)
