n=int(input())
ans=[0]*301
stair=[]
for i in range(n):
  a=int(input())
  stair.append(a)
ans[0]=stair[0]
for j in range(1,n):
  ans[j]=max(ans[j-3]+stair[j-1]+stair[j],ans[j-2]+stair[j])

print(ans[n-1]) ##중요