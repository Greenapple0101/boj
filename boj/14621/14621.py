import sys

input = sys.stdin.readline

N, M = map(int, input().split())
schools = input().split()
edges = []
for _ in range(M):
    u, v, d = map(int, input().split())
    if (schools[u - 1] != schools[v - 1]): edges.append((d, u, v))

parent = [i for i in range(N + 1)]


def find_parent(x):
    if (parent[x] != x):
        parent[x] = find_parent(parent[x])
    return parent[x]


rank = [0] * (N + 1)


def union(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if (a == b):
        return False
    else:
        if (rank[a] > rank[b]):
            parent[b] = a
        elif (rank[a] < rank[b]):
            parent[a] = b
        else:
            parent[a] = b
            rank[b] += 1
    return True


ans = 0
count = 0
edges.sort()

for w, u, v in edges:
    if (union(u, v)):
        ans += w
        count += 1
        if (count == N - 1):
            break

if (count != N - 1):
    print(-1)
else:
    print(ans)

