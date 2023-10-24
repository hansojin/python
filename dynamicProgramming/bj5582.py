s1, s2 = list(input()), list(input())

len_s2 = len(s2)
pre_dp = [0]*(len_s2+1)
ans = 0

for i in range(1, len(s1)+1):
    now_dp = [0]*(len_s2+1)
    for j in range(1, len_s2+1):
        if s1[i-1] == s2[j-1]:
            now_dp[j] = pre_dp[j-1]+1
    ans = max(ans, max(now_dp))
    pre_dp = now_dp

print(ans)

