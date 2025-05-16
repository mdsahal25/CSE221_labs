import heapq
from collections import defaultdict
def distance(a,b,c,d,zb,zy,zt):
    g=defaultdict(list)
    for u, v, w in zip(zb,zy,zt):
      g[u].append((v, w))
    dist=[float('inf')] * (a + 1)
    prev=[-1]*(a + 1)
    dist[c] = 0
    heap=[(0,c)]
    while heap:
      m, n = heapq.heappop(heap)
      if m > dist[n]:
        continue
      for neighbor, weight in g[n]:
        if dist[n] + weight < dist[neighbor]:
          dist[neighbor] = dist[n] + weight
          prev[neighbor] = n
          heapq.heappush(heap,(dist[neighbor],neighbor))

    if dist[d] == float('inf'):
        print(-1)
        return

    print(dist[d])
    path = []
    apt =d
    while apt != -1:
      path.append(apt)
      apt = prev[apt]
    path.reverse()
    print(' '.join(map(str, path)))

a,b,c,d=list(map(int, input().split()))
zb=list(map(int, input().split()))
zy=list(map(int, input().split()))
zt=list(map(int, input().split()))
distance(a,b,c,d,zb,zy,zt)
