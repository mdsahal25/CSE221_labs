def mod_expo(b, e, m):
   r = 1
   while e > 0:
       if e % 2 == 1:
           r = (r * b) % m
       b = (b * b) % m
       e //= 2
   return r
def geo_sum(a, n, m):
   if a == 1:
       return n % m
   n = mod_expo(a, n + 1, m * (a - 1)) - a
   d = a - 1
   return (n // d) % m
t = int(input())
for i in range(t):
   a, n, m = map(int, input().split())
   print(geo_sum(a, n, m))