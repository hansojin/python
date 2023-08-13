#!/usr/bin/env python

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    result = -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] <= target:
            result = mid
            left = mid + 1
        else:
            right = mid - 1
    return result

n, m = map(int, input().split())
a_tier = list(map(int, input().split()))
b_tier = list(map(int, input().split()))

a_tier.sort()

a_wins = 0
b_wins = 0
draws = 0

for b in b_tier:
    wins = binary_search(a_tier, b)
    a_wins += wins
    b_wins += n - wins
    draws += 1

draws -= a_wins + b_wins

print(a_wins, b_wins, draws)

