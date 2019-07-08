k2=int(input())
l2=list(map(int,input().split()))
mi2=max(l2)
a2,b2=0,0
for i2 in range(0,len(l2)-1):
  for j2 in range(i2+1,len(l2)):
    if abs(l2[i2]+l2[j2])<mi2:
      a2,b2=l2[i2],l2[j2]
      mi2=abs(a2+b2)
print(a2,b2)
