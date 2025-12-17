t=int(input())
for i in range(t):
    B1,B2,B3=map(int,input().split())
    if B1+B2+B3 <= 1:
        print("Water Filling Time")
    else:
        print("Not Now")