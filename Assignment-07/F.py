import heapq
a,b,c,d=map(int,input().split())
m=[[]for _ in range(a+1)]
for i in range(b):
  u,v,w=map(int,input().split())
  m[u].append((v,w))
  m[v].append((u,w))
di=[[float("inf"),float("inf")] for j in range(a+1)]
di[c][0]=0
rt=[(0,c)]
while rt:
  co,u=heapq.heappop(rt)
  for v,w in m[u]:
    nco=co+w
    if nco<di[v][0]:
      di[v][1]=di[v][0]
      di[v][0]=nco
      heapq.heappush(rt,(nco,v))
    elif di[v][0]<nco<di[v][1]:
      di[v][1]=nco
      heapq.heappush(rt,(mco,v))
if di[d][1]==float("inf"):
  print(-1)
else:
  print(di[d][1])