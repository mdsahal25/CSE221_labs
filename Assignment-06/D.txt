import sys
sys.setrecursionlimit(2*10**5)
N,R=map(int,input().split())
g = []
for i in range(N + 1):
    g.append([])

for i in range(N-1):
    u,v=map(int,input().split())
    g[u].append(v)
    g[v].append(u)
size=[0]*(N+1)
visited=[0]*(N+1)
def dfs(x):
    visited[x]=0
    size[x]=1
    for j in g[x]:
        if not visited[j]:
            dfs(j)
            size[x]+=size[j]
dfs(R)
Q=int(input())
for i in range(Q):
    print(size[int(input())])