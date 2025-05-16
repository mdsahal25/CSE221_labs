def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
N, Q = map(int, input().split())
G = [[] for i in range(N + 1)]
for i in range(1, N + 1):
    for j in range(1, N + 1):
        if i != j and gcd(i, j) == 1:
            G[i].append(j)
    G[i].sort() 
for i in range(Q):
    X, K = map(int, input().split())
    if K <= len(G[X]):
        print(G[X][K - 1])
    else:
        print(-1)