import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
m, n = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(m)]
dy = [-1, 1, 0, 0]
dx = [0, 0, 1, -1]
dp = [[-1] * n for _ in range(m)]


def dfs(i, j):
    if i == m - 1 and j == n - 1:
        return 1
    if (dp[i][j] != -1): return dp[i][j]
    dp[i][j] = 0
    for k in range(4):
        ni = i + dy[k]
        nj = j + dx[k]
        if (0 <= ni < m and 0 <= nj < n):
            if (grid[ni][nj] < grid[i][j]):
                dp[i][j] += dfs(ni, nj)
    return dp[i][j]


print(dfs(0, 0))
