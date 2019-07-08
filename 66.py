dem=int(input())
arr=list(map(int,input().split()))
c=len(arr)
big=max(arr)
g,h=0,0
for i in range(0,c-1):
    for j in range(i+1,c):
        if abs(arr[i]+arr[j])< big:
            g,h=arr[i],arr[j]
            big=abs(g+h)
print(g,h)

