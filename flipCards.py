t=int(input())
for i in range(t):
    N,X=map(int,input().split())
    if X==0 or N==X:
        print(0)
    elif X<=N-X:
        print(X)
    else:
        print(N-X)