import math

t=int(input())
for i in range(t):
    N,X=map(int,input().split())
    print(math.ceil(N/6) * X)