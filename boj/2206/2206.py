from collections import deque

N, M = map(int, input().split())
dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]
grid = [list(map(int, input().strip())) for _ in range(N)]
visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]


def bfs():
    q = deque([(0, 0, 0, 1)])
    visited[0][0][0] = 1
    while q:
        y, x, wall, dist = q.popleft()
        for i in range(4):
            if (y == N - 1 and x == M - 1): return dist
            ny = y + dy[i]
            nx = x + dx[i]
            if (ny < 0 or ny >= N or nx < 0 or nx >= M or visited[ny][nx][wall]): continue
            if (grid[ny][nx] == 1):
                if (wall): continue
                q.append((ny, nx, 1, dist + 1))
                visited[ny][nx][wall] = 1
            else:
                q.append((ny, nx, wall, dist + 1))
                visited[ny][nx][wall] = 1
    return -1


print(bfs())