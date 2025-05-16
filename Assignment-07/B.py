import heapq
import heapq
import sys
def dijkstra(n, graph, S, T):
    dist_alice = [sys.maxsize] * (n + 1)
    dist_bob = [sys.maxsize] * (n + 1)
    dist_alice[S] = 0
    dist_bob[T] = 0
    pq = []
    heapq.heappush(pq, (0, S, 'A'))
    heapq.heappush(pq, (0, T, 'B'))
    while pq:
        current_dist, node, who = heapq.heappop(pq)
        if who == 'A' and current_dist > dist_alice[node]:
         continue
        if who == 'B' and current_dist > dist_bob[node]:
          continue
        if who == 'A':
          dist = dist_alice
        else:
          dist = dist_bob

        for neighbor, weight in graph[node]:
            new_dist = current_dist + weight
            if new_dist < dist[neighbor]:
              dist[neighbor] = new_dist
              heapq.heappush(pq, (new_dist, neighbor, who))

    return dist_alice, dist_bob

def solve():
    n, m, S, T = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
      u, v, w = map(int, input().split())
      graph[u].append((v, w))
    dist_alice, dist_bob = dijkstra(n, graph, S, T)
    min_time = sys.maxsize
    best_node = -1
    for node in range(1, n + 1):
      if dist_alice[node] != sys.maxsize and dist_bob[node] != sys.maxsize:
        meeting_time = max(dist_alice[node], dist_bob[node])
        if meeting_time < min_time or (meeting_time == min_time and node < best_node):
          min_time = meeting_time
          best_node = node
    if best_node == -1:
      print(-1)
    else:
      print(min_time, best_node)

solve()