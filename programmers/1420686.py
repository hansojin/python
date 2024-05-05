def solution(s):
    answer = []
    visited = {}

    for i, c in enumerate(s):
        if c in visited:
            diff = i - visited[c] + 1
            answer.append(diff)
            visited[c] = i + 1
        else:
            answer.append(-1)
            visited[c] = i + 1

    return answer
