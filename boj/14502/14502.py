from collections import deque

n, m = map(int, input().split())
map_data = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
max_ans = 0
dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]


def bfs(i, j, temp_data):
    q = deque([(i, j)])
    while q:
        y, x = q.popleft()
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            if (0 <= ny < n and 0 <= nx < m and temp_data[ny][nx] == 0):
                temp_data[ny][nx] = 2
                q.append((ny, nx))


def island_size(temp_data):
    sum = 0
    for i in range(n):
        for j in range(m):
            if (temp_data[i][j] == 2):
                bfs(i, j, temp_data)
    for i in range(n):
        for j in range(m):
            if (temp_data[i][j] == 0):
                sum += 1
    return sum


lst = []
for i in range(n):
    for j in range(m):
        if (map_data[i][j] == 0):
            lst.append((i, j))

visited_d = [0] * len(lst)


def select(cnt, start):
    global max_ans
    if (cnt == 3):  ##이건 트리랑 다르다. cnt는 3이상으로 갈수가 있다
        temp_map = [row[:] for row in map_data]
        max_ans = max(max_ans, island_size(temp_map))
        return
    for k in range(start, len(lst)):
        yy, xx = lst[k]
        if (visited_d[k] == 0):
            visited_d[k] = 1
            map_data[yy][xx] = 1
            select(cnt + 1, k + 1)
            visited_d[k] = 0
            map_data[yy][xx] = 0


select(0, 0)
print(max_ans)