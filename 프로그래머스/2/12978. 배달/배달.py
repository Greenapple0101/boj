import heapq
def solution(N, road, K):
    graph = [[] for _ in range(N + 1)]
    for a, b, c in road:
        graph[a].append((b, c))
        graph[b].append((a, c))
    INF = float('inf')
    dist = [INF] * (N + 1)
    dist[1] = 0
    heap = [(0, 1)]
    while heap:
        cur_dist, cur_node = heapq.heappop(heap)
        if cur_dist > dist[cur_node]:
            continue
        for next_node, cost in graph[cur_node]:
            new_dist = cur_dist + cost
            if new_dist < dist[next_node]:
                dist[next_node] = new_dist
                heapq.heappush(heap, (new_dist, next_node))
    return sum(d <= K for d in dist)