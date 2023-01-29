#!/usr/bin/env python

a,b=map(str,input().split())

aa=''.join(reversed(a))
bb=''.join(reversed(b))

print(max(aa,bb))
