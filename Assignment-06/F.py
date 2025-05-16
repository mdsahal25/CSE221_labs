from collections import deque,defaultdict
N=int(input())
a=[input() for _ in range(N)]
g=[[] for _ in range(26)]
ind=[0]*26
used=[0]*26
for i in range(N-1):
    w1,w2=a[i],a[i+1]
    m=min(len(w1),len(w2))
    found=False
    for j in range(m):
        if w1[j]!=w2[j]:
            u,v=ord(w1[j])-97,ord(w2[j])-97
            g[u].append(v)
            ind[v]+=1
            found=True
            break
    if not found and len(w1)>len(w2):
        print(-1)
        exit()
for s in a:
    for c in s:
        used[ord(c)-97]=1
q=deque(i for i in range(26) if ind[i]==0 and used[i])
res=[]
while q:
    x=min(q)
    q.remove(x)
    res.append(x)
    for v in g[x]:
        ind[v]-=1
        if ind[v]==0:
            q.append(v)
if len(res)!=sum(used): print(-1)
else: print(''.join(chr(x+97) for x in res))