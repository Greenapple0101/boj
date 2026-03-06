from collections import deque

k = int(input())  # 원숭이가 말처럼 움직이는 횟수
w, h = map(int, input().split())
d1y = [1, 1, -1, -1, 2, 2, -2, -2, 1, -1, 0, 0]
d1x = [2, -2, 2, -2, 1, -1, 1, -1, 0, 0, 1, -1]
d2y = [1, -1, 0, 0]
d2x = [0, 0, 1, -1]


def bfs():
    q = deque([(0, 0, 0, 0)])
    visited = [[[0] * (k + 1) for _ in range(w)] for _ in range(h)]
    visited[0][0][0] = 1
    while q:
        y, x, count, count2 = q.popleft()
        if (y == h - 1 and x == w - 1):
            return count
        if (count2 < k):
            for i in range(12):
                ny = y + d1y[i]
                nx = x + d1x[i]
                if (0 <= ny < h and 0 <= nx < w and grid[ny][nx] == 0):
                    if (i < 8):
                        if (visited[ny][nx][count2 + 1] == 1): continue
                        visited[ny][nx][count2 + 1] = 1
                        q.append((ny, nx, count + 1, count2 + 1))
                    else:
                        if (visited[ny][nx][count2]): continue
                        visited[ny][nx][count2] = 1
                        q.append((ny, nx, count + 1, count2))
        else:
            for p in range(4):
                ny = y + d2y[p]
                nx = x + d2x[p]
                if (0 <= ny < h and 0 <= nx < w and visited[ny][nx][count2] == 0 and grid[ny][nx] == 0):
                    visited[ny][nx][count2] = 1
                    q.append((ny, nx, count + 1, count2))
    return -1


grid = []
for _ in range(h):  # 0은 평지, 1은 장애물
    row = list(map(int, input().split()))
    grid.append(row)

print(bfs())
