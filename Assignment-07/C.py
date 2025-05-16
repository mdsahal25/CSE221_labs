import sys
import heapq
from collections import defaultdict
input = sys.stdin.readline

def minimum_danger(n, m, edges):
    graph = defaultdict(list)
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))
    dist = [float('inf')] * (n + 1)
    dist[1] = 0
    heap = [(0, 1)]
    while heap:
        danger, node = heapq.heappop(heap)
        if danger > dist[node]:
            continue
        for neighbor, weight in graph[node]:
            new_danger = max(danger, weight)
            if new_danger < dist[neighbor]:
                dist[neighbor] = new_danger
                heapq.heappush(heap, (new_danger, neighbor))
    res = [0 if i == 1 else (dist[i] if dist[i] != float('inf') else -1) for i in range(1, n + 1)]
    print(' '.join(map(str, res)))

n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
minimum_danger(n, m, edges)