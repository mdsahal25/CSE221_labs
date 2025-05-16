def power(a,b,mod):
    if b==0:
        return 1
    mid=b//2
    c=power(a,mid,mod)%mod
    c=(c*c)%mod
    if b%2==0:
        return c
    else:
        return (a*c)%mod
a,b=input().split()
print(power(int(a),int(b),107))