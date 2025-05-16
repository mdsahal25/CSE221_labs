from collections import deque
N=int(input())
g=[[] for _ in range(N+1)]
for i in range(N-1):
    u,v=map(int,input().split())
    g[u].append(v)
    g[v].append(u)
def bfs(s):
    visited=[-1]*(N+1)
    q=deque()
    q.append(s)
    visited[s]=0
    diameter=(0,s)
    while q:
        x=q.popleft()
        for k in g[x]:
            if visited[k]==-1:
                visited[k]=visited[x]+1
                q.append(k)
                if visited[k]>diameter[0]: diameter=(visited[k],k)
    return diameter
d1,x=bfs(1)
d2,y=bfs(x)
print(d2)
print(x,y)