n=int(input())
graph=[]
for _ in range(n):
    a=[0]*n
    graph.append(a)
for i in range(n):
    lst=list(map(int,input().split()))
    for j in range(1,lst[0]+1):
        graph[i][lst[j]]=1
for j in range(n):
    for k in range(n):
        print(graph[j][k],end=' ')
    print()    