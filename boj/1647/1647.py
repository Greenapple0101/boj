n, m = map(int, input().split())
edges = []
for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append([c, a, b])

parent = [i for i in range(n + 1)]


def find_parent(x):
    if (parent[x] != x):
        parent[x] = find_parent(parent[x])
    return parent[x]


rank = [0] * (n + 1)


def union(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if (a == b):
        return False
    if (rank[a] > rank[b]):
        parent[b] = a
    elif (rank[b] > rank[a]):
        parent[a] = b
    else:
        parent[a] = b
        rank[a] = +1
    return True


edges.sort()
ans = []
to_minus = []

weight = 0
node_count = 0
for c, a, b in edges:
    if (union(a, b)):
        to_minus.append(c)
        weight += c
        node_count += 1
        if (node_count == n - 1):
            break

print(weight - max(to_minus))

