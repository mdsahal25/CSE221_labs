import heapq
def alternating_path(N, adjacency_list):
    d= [[float('inf')] * 2 for _ in range(N + 1)]
    d[1][0] = 0
    d[1][1] = 0
    pq = [(0, 1, -1)]
    while pq:
        path_cost, current_node, ly = heapq.heappop(pq)
        for next_node, edge_weight in adjacency_list[current_node]:
            current_parity = edge_weight % 2
            if current_parity == ly:
                continue
            total_cost = path_cost + edge_weight
            if total_cost < d[next_node][current_parity]:
                d[next_node][current_parity] = total_cost
                heapq.heappush(pq, (total_cost, next_node, current_parity))
    best_cost = min(d[N])
    return -1 if best_cost == float('inf') else best_cost
N, M = map(int, input().split())
adjacency_list = [[] for i in range(N + 1)]
u = list(map(int, input().split()))
v = list(map(int, input().split()))
w = list(map(int, input().split()))
for i in range(M):
   adjacency_list[u[i]].append((v[i], w[i]))
result = alternating_path(N, adjacency_list)
print(result)