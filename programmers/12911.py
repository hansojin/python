def solution(n):
    i = n + 1
    while True:
        if bin(i)[2:].count('1') == bin(n)[2:].count('1'):
            break
        i += 1
    return i
