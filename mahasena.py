N=int(input())
array=[]
luckySoldiers = 0
for i in range(N):
    soldier=int(input())
    array.append(soldier)
    if array[i]%2 == 0:
        luckySoldiers = luckySoldiers + 1
unluckySoldiers = N - luckySoldiers
if luckySoldiers > unluckySoldiers:
    print("READY FOR BATTLE")
else:
    print("NOT READY")