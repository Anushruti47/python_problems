t=int(input())
for i in range(t):
    A,B=map(int,input().split())
    valuationA=A*100//10
    valuationB=B*100//20
    if valuationA>valuationB:
        print("FIRST")
    elif valuationB>valuationA:
        print("SECOND")
    else:
        print("ANY")