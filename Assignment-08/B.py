def find(parent,x):
    if parent[x]!=x:
        parent[x]=find(parent,parent[x])
    return parent[x]
def union(parent,rank,x,y):
    root_x=find(parent,x)
    root_y=find(parent,y)
    if root_x==root_y:
        return False
    if rank[root_x]<rank[root_y]:
        parent[root_x]=root_y
    else:
        parent[root_y]=root_x
        if rank[root_x]==rank[root_y]:
            rank[root_x]+=1
    return True
def kruskal(n,edges):
    parent=[i for i in range(n+1)]
    rank=[0]*(n+1)
    edges.sort(key=lambda x:x[2])
    mst_cost=0
    edges_used=0
    for u,v,w in edges:
        if union(parent,rank,u,v):
            mst_cost+=w
            edges_used+=1
            if edges_used==n-1:
                break
    return mst_cost
N,M=map(int,input().split())
edges = []
for _ in range(M):
    u,v,w=map(int,input().split())
    edges.append((u,v,w))
print(kruskal(N,edges))