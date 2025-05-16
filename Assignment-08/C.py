import sys
from sys import stdin
def secondbest():
    N, M = map(int, input().split())
    edges = []
    for i in range(M):
        u, v, w = map(int, input().split())
        edges.append((w, u, v))
    edges.sort()
    def kruskal(exclude_edge=None):
        total = 0
        mst_edges = []
        parent_copy = list(range(N + 1))
        def find_copy(u):
            while parent_copy[u] != u:
                parent_copy[u] = parent_copy[parent_copy[u]]
                u = parent_copy[u]
            return u
        for i, (w, u, v) in enumerate(edges):
            if exclude_edge is not None and i == exclude_edge:
                continue
            root_u = find_copy(u)
            root_v = find_copy(v)
            if root_u != root_v:
                parent_copy[root_v] = root_u
                total += w
                mst_edges.append((w, u, v))
        if len(mst_edges) != N - 1:
            return None
        return total
    best_mst = kruskal()
    if best_mst is None:
        print(-1)
        return
    second_best = float('inf')
    parent_best = list(range(N + 1))
    def find_best(u):
        while parent_best[u] != u:
            parent_best[u] = parent_best[parent_best[u]]
            u = parent_best[u]
        return u
    mst_edge_indices = []
    for i, (w, u, v) in enumerate(edges):
        root_u = find_best(u)
        root_v = find_best(v)
        if root_u != root_v:
            parent_best[root_v] = root_u
            mst_edge_indices.append(i)
    for excluded_edge in mst_edge_indices:
        current_mst = kruskal(excluded_edge)
        if current_mst is not None and current_mst > best_mst:
            if current_mst < second_best:
                second_best = current_mst
    non_mst_edges = [i for i in range(M) if i not in mst_edge_indices]
    for edge in non_mst_edges:
        w, u, v = edges[edge]
        temp_parent = list(range(N + 1))
        def find_temp(u):
            while temp_parent[u] != u:
                temp_parent[u] = temp_parent[temp_parent[u]]
                u = temp_parent[u]
            return u
        temp_parent[find_temp(u)] = find_temp(v)
        used_edges = 1
        total = w
        for i in mst_edge_indices:
            w_mst, u_mst, v_mst = edges[i]
            root_u = find_temp(u_mst)
            root_v = find_temp(v_mst)
            if root_u != root_v:
                temp_parent[root_v] = root_u
                total += w_mst
                used_edges += 1
        if used_edges == N - 1 and total > best_mst and total < second_best:
            second_best = total
    if second_best == float('inf'):
        print(-1)
    else:
        print(second_best)
secondbest()