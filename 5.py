N=int(input())
l=list(map(int,input().split()))
for i in range(len(l)):
    for j in range(len(l)):
        for k in range(len(l)):
            if i<j<k:
                if l[i]+l[j]==l[k]:
                    print(l[i],l[j],l[k])
