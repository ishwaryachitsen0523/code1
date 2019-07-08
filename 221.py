n=input()
k=1
for j in range(len(n)-1):
    s=n[j]+n[j+1]
    p=int(s)
    if p<=26 and n[j]!="0":
        k+=1
if k==3:
    print(k)
else:
    print(k+(k-1)//2)
