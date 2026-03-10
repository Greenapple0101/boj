n, m = map(int, input().split())
path = []
visited_col = [0] * (n + 2)


def dfs(level, start):
    if (level == m):
        print(*path)
        return

    for i in range(start, n):
        if (visited_col[i] == 0):
            path.append(i + 1)
            visited_col[i] = 1
            dfs(level + 1, i)
            path.pop()
            visited_col[i] = 0


dfs(0, 0)