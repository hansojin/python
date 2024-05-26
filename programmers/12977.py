import math
from itertools import combinations
def prime_numbers():
    n=3000
    arr = [i for i in range(n+1)] 
    end = int(n**(1/2))
    for i in range(2, end+1):
        if arr[i] == 0: 
            continue
        for j in range(i*i, n+1, i):
            arr[j] = 0
            
    return [i for i in arr[2:] if arr[i]]
    
def solution(nums):
    p=prime_numbers()
    answer = 0
    for x in combinations(nums,3):
        if sum(x) in p:
            answer+=1
    return answer
