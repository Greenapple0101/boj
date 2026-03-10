n = int(input())
score = [list(map(int, input().split())) for _ in range(n)]
visited = [0] * n
ans = 0
minn = 1e9


def dfs(level, start):
    global minn, ans
    if (level == n // 2):
        scorea = 0
        scoreb = 0
        for i in range(n):
            for j in range(n):
                if (visited[i] and visited[j]):
                    scorea += score[i][j]
                if (visited[i] == 0 and visited[j] == 0):
                    scoreb += score[i][j]
        ans = abs(scorea - scoreb)
        minn = min(ans, minn)
        return

    for i in range(start, n):
        visited[i] = 1
        dfs(level + 1, i + 1)
        visited[i] = 0

    return minn


visited[0] = 1
print(dfs(0, 0))