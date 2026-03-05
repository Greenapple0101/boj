from collections import deque
n=int(input())
work=[[] for _ in range(n)]
time=[0]*(n)
jinip=[0]*n
result=[0]*n
for i in range(n):
  lst=list(map(int,input().split()))
  for k in range(len(lst)-2):
    work[i].append(lst[k+2])
    jinip[i]+=1
  time[i]=lst[0]
ans=0

def topology():
  global ans,result
  q=deque()
  for i in range(n):
    if(jinip[i]==0):
      q.append(i)
      result[i]=time[i]
  while q:
    l=q.popleft()
    print(l)
    for k in range(n):
      if(l+1 in work[k]):
        result[k]=max(result[k],result[l]+time[k])
        print(result)
        jinip[k]-=1
        if(jinip[k]==0):
          q.append(k)

topology()