n, m = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
path = []
visited_col = [0] * (n + 2)


def dfs(level, start):
    if (level == m):
        print(*path)
        return

    for i in range(n):
        path.append(lst[i])
        visited_col[i] = 1
        dfs(level + 1, i)
        path.pop()
        visited_col[i] = 0


dfs(0, 0)