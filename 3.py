p=int(input())
q=list(map(int,input().split()))
q.sort():
m=[]
for i in range(len(q)-1):
  if q[i]==q[i+1]:
    m.append(q[i])
    break
if m:
  for x in set(m):
    print(x,end=" " )
else:
  print("unique")
