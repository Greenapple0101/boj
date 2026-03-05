n = int(input())
m = int(input())
parent = [i for i in range(n + 1)]


def find_parent(a):
    if (parent[a] != a):
        parent[a] = find_parent(parent[a])
    return parent[a]


def union(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if (a == b):
        return False
    else:
        if (rank[a] > rank[b]):
            parent[b] = a
        elif (rank[b] > rank[a]):
            parent[a] = b
        else:
            parent[a] = b
            rank[b] += 1
        return True


edges = []
ans_weight = 0
edge_count = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append([c, a, b])

edges.sort()
rank = [0] * (n + 1)

for c, a, b in edges:
    if (union(a, b)):
        ans_weight += c
        edge_count += 1
        if edge_count == n - 1:
            break

print(ans_weight)