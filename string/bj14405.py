#!/usr/bin/env python

n=input().rstrip()
n=n.replace('pi','').replace("ka",'').replace('chu','')
print("YES" if len(n.strip())==0 else "NO")
