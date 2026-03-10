n, m = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
# 일단 조합
visited = [0] * (len(lst) + 1)


def dfs(level, start, path):
    if (level == m):
        print(*path)
        return

    last_val = -1
    for i in range(start, len(lst)):
        if (last_val == lst[i]): continue
        if (visited[i]): continue
        visited[i] = 1
        last_val = lst[i]
        dfs(level + 1, i, path + [lst[i]])
        visited[i] = 0


dfs(0, 0, [])
