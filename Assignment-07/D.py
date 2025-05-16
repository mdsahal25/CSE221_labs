import sys
import heapq
from collections import defaultdict
input = sys.stdin.readline

def shortest_path(n, m, s, d, weights, edges):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
    dist = [float('inf')] * (n + 1)
    prev = [-1] * (n + 1)
    dist[s] = weights[s - 1]
    heap = [(weights[s - 1], s)]
    while heap:
        cost, node = heapq.heappop(heap)
        if cost > dist[node]:
            continue
        for neighbor in graph[node]:
            if dist[node] + weights[neighbor - 1] < dist[neighbor]:
                dist[neighbor] = dist[node] + weights[neighbor - 1]
                prev[neighbor] = node
                heapq.heappush(heap, (dist[neighbor], neighbor))
    if dist[d] == float('inf'):
        print(-1)
        return
    print(dist[d])
    path = []
    cur = d
    while cur != -1:
        path.append(cur)
        cur = prev[cur]
    path.reverse()
    print(' '.join(map(str, path)))

n, m, s, d = map(int, input().split())
weights = list(map(int, input().split()))
edges = [tuple(map(int, input().split())) for _ in range(m)]
shortest_path(n, m, s, d, weights, edges)