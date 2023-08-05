#!/usr/bin/env python

import sys
input= sys.stdin.readline
def quick_sort(arr):
    cnt = 0

    if len(arr) <= 1:
        return arr, cnt

    pivot = arr[len(arr) // 2]
    less, equal, greater = [], [], []

    for num in arr:
        cnt += 1
        if num < pivot:
            less.append(num)
        elif num > pivot:
            greater.append(num)
        else:
            equal.append(num)

    sorted_less, cnt_less = quick_sort(less)
    sorted_greater, cnt_greater = quick_sort(greater)

    return sorted_less + equal + sorted_greater, cnt + cnt_less + cnt_greater

def main():
    N = int(input())
    A = list(map(int, input().split()))

    _, cnt = quick_sort(A)
    print(cnt)

if __name__ == "__main__":
    main()

