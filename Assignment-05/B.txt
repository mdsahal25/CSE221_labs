import sys
sys.setrecursionlimit(2 * 100000 + 5)
N, M = map(int, input().split())
lst1 = list(map(int, input().split()))
lst2 = list(map(int, input().split()))
graph = {}
for i in range(1, N + 1):
    graph[i] = []
for i in range(M):
    u = lst1[i]
    v = lst2[i]
    graph[u].append(v)
    graph[v].append(u) 
for node in graph:
    graph[node].sort()
visited = [False] * (N + 1)
traversal = []
def dfs(node):
    visited[node] = True
    traversal.append(node)
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs(neighbor)
dfs(1)
print(*traversal)