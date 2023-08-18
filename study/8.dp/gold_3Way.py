# 채굴자는 첫 번째 열부터 출발하여 금을 캐기 시작한다. 맨 처음에는 첫 번째 열의 어느 행에서든 출발할 수 있다.
# 이후에 m - 1번에 걸쳐서 매번 오른쪽 위, 오른쪽, 오른쪽 아래 3가지 중 하나의 위치로 이동해야 한다.
# 결과적으로 채굴자가 얻을 수 있는 금의 최대 크기를 출력하는 프로그램을 작성하라

# 문제 해결 아이디어
# 사실 금광의 모든 위치에 대하여 다음의 세 가지만 고려하면 된다
# 1. 왼쪽 위에서 오는 경우
# 2. 왼쪽 아래에서 오는 경우
# 3. 왼쪽에서 오는 경우

# 즉, dp table에 1열만 가져오고, 그 이후는 전 열의 max 값에 자기값을 더한 값을 더하면 됨

# 테스트 케이스(Test Case) 입력
for tc in range(int(input())):
    # 금광 정보 입력
    n, m = map(int, input().split())
    array = list(map(int, input().split()))

    # 다이나믹 프로그래밍을 위한 2차원 DP 테이블 초기화
    dp = []
    index = 0
    for i in range(n):
        dp.append(array[index:index + m])
        index += m

    # 다이나믹 프로그래밍 진행
    for j in range(1, m):
        for i in range(n):
            # 왼쪽 위에서 오는 경우
            if i == 0:
                left_up = 0
            else:
                left_up = dp[i - 1][j - 1]
            # 왼쪽 아래에서 오는 경우
            if i == n - 1:
                left_down = 0
            else:
                left_down = dp[i + 1][j - 1]
            # 왼쪽에서 오는 경우
            left = dp[i][j - 1]
            dp[i][j] = dp[i][j] + max(left_up, left_down, left)

    result = 0
    for i in range(n):
        result = max(result, dp[i][m - 1])

    print(result)
