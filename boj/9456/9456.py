import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    dp = [[0] * n for i in range(2)]
    score = [list(map(int, input().split())) for i in range(2)]
    dp[0][0] = score[0][0]
    dp[1][0] = score[1][0]
    dp[0][1] = score[1][0] + score[0][1]
    dp[1][1] = score[0][0] + score[1][1]
    for i in range(2, n):
        dp[0][i] = max(dp[1][i - 1], dp[1][i - 2]) + score[0][i]
        dp[1][i] = max(dp[0][i - 1], dp[0][i - 2]) + score[1][i]

    print(max(dp[0][n - 1], dp[1][n - 1]))