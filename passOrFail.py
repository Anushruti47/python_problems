t=int(input())
for i in range(t):
    N,X,P=map(int,input().split())
    if (X*3 - (N-X)*1) >= P:
        print("PASS")
    else:
        print("FAIL")
        