def solution(n, arr1, arr2):
    map =  [
            bin(i | j)[2:].zfill(n).replace("1", "#").replace("0", " ")
            for i, j in zip(arr1, arr2)
    ]
    return map
