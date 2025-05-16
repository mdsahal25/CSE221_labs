N = input()
N = N.split(' ') 
N1 = int(N[0])
N2 = int(N[1])
K = input()
K = K.split(' ')
New = (K[(N2-1)::-1])
for i in New:
    print(int(i),end=' ')