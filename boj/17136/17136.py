grid = [list(map(int, input().split())) for _ in range(10)]
paper = [5] * 5
lst = []
for i in range(10):
    for j in range(10):
        if (grid[i][j] == 1):
            lst.append((i, j))


def can_stick(y, x, size):
    if (y + size > 10 or x + size > 10): return False
    for i in range(y, y + size):
        for j in range(x, x + size):
            if (grid[i][j] == 0): return False
    return True


def cover(y, x, size, val):
    for i in range(y, y + size):
        for j in range(x, x + size):

            if (grid[i][j] != val):
                grid[i][j] = val


ans = 1e9


def dfs(idx, count):
    global ans
    if (count >= ans): return
    if (idx == len(lst)):
        ans = min(ans, count)
        return
    a, b = lst[idx]
    if (grid[a][b] == 0):
        dfs(idx + 1, count)
        return
    for s in range(5, 0, -1):
        if (paper[s - 1] <= 0 or can_stick(a, b, s) == 0): continue
        paper[s - 1] -= 1
        cover(a, b, s, 0)
        dfs(idx + 1, count + 1)
        paper[s - 1] += 1
        cover(a, b, s, 1)


dfs(0, 0)
if (ans == 1e9):
    print(-1)
else:
    print(ans)