def search_func(x):
    while p[x] != x:
        p[x] = p[p[x]]
        x = p[x]
    return x

def connect(x, y):
    x_root = search_func(x)
    y_root = search_func(y)
    if x_root!=y_root:
        if t_size[x_root] < t_size[y_root]:
            x_root, y_root = y_root, x_root
        p[y_root] = x_root
        t_size[x_root]+=t_size[y_root]
    return t_size[x_root]

N, K = map(int, input().split())
p = [i for i in range(N+1)]
t_size = [1]*(N+1)

for i in range(K):
    a, b = map(int, input().split())
    result = connect(a, b)
    print(result)