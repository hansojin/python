#!/usr/bin/env python

import sys
input= sys.stdin.readline

def quicksort(arr):
    if len(arr) <= 1:
        return arr, 0

    less = []
    greater = []
    pivot = arr[len(arr) // 2]
    cnt = 0

    for element in arr:
        cnt += 1
        if element < pivot:
            less.append(element)
        elif element > pivot:
            greater.append(element)

    sorted_less, cnt_less = quicksort(less)
    sorted_greater, cnt_greater = quicksort(greater)

    return sorted_less + [pivot] + sorted_greater, cnt + cnt_less + cnt_greater

n = int(input())
arr = list(map(int, input().split()))

sorted_arr, cnt = quicksort(arr)

print(cnt)

