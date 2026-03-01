import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
adj = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

parent = [0] * (N + 1)
visited = [0] * (N + 1)


def dfs(n):
    q = deque([n])
    visited[n] = 1
    while (q):
        curr = q.popleft()
        for val in adj[curr]:
            if not visited[val]:
                visited[val] = 1
                parent[val] = curr
                q.append(val)


dfs(1)
for i in range(2, N + 1):
    print(parent[i])


