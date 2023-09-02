#!/usr/bin/env python

A, B, C = map(int, input().split())
print(A * max(B, C) // min(B, C))
