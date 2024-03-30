def solution(s):
    li=list(map(int,s.split(" ")))
    return f'{min(li)} {max(li)}'
