#!/usr/bin/env python

sb = []
num_tests = int(input())

for _ in range(num_tests):
    left = 1
    right = int(1e9)

    n = int(input())
    exp = n * (n + 1) // 2

    while left <= right:
        mid = (left + right) // 2
        if mid * (mid + 1) <= exp:
            left = mid + 1
        else:
            right = mid - 1

    sb.append(str(left) + "\n")

print("".join(sb))

