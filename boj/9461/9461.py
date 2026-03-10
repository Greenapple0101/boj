import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    if (N <= 3):
        print(1)
        continue
    dp = [0] * (N + 1)
    dp[0] = 1
    dp[1] = 1
    dp[2] = 1

    for i in range(3, N):
        dp[i] = dp[i - 2] + dp[i - 3]

    print(dp[N - 1])