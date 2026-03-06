n = int(input())
grid = [[0] * n for _ in range(n)]
dx = [1, -1, 1, -1]
dy = [1, -1, -1, 1]

colv = [0] * n
diag_down = [0] * 2 * n
diag_up = [0] * 2 * n
ans = 0


def dfs(row):
    global ans
    if (row == n):
        ans += 1
        return

    for col in range(n):
        dd = row - col + (n - 1)
        du = row + col
        if (diag_down[dd] or diag_up[du] or colv[col]): continue
        colv[col] = 1
        diag_down[dd] = 1
        diag_up[du] = 1
        dfs(row + 1)
        colv[col] = 0
        diag_down[dd] = 0
        diag_up[du] = 0


dfs(0)
print(ans)
