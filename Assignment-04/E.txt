n,m=input().split()
n=int(n)
m=int(m)
begin=list(map(int,input().split()))
end=list(map(int,input().split()))
out_degree=[0]*n
in_degree=[0]*n
for i in range(m):
    u=begin[i]-1
    v=end[i]-1
    out_degree[u]+=1
    in_degree[v]+=1
for j in range(n):
    temp = in_degree[j]-out_degree[j]
    print(temp,end=' ')