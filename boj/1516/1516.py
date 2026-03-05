from collections import deque
n=int(input())
time=[0]*n
jinip=[0]*n
result=[0]*n
adj=[[] for _ in range(n)]
for i in range(n):
  lst=list(map(int,input().split()))
  time[i]=lst[0]
  for k in lst[1:-1]:
    adj[k-1].append(i)
    jinip[i]+=1

def topology():
  q=deque()
  for j in range(n):
    if(jinip[j]==0):
      q.append(j)
      result[j]=time[j]
  while q:
    now=q.popleft()
    for curr in adj[now]:
      jinip[curr]-=1
      result[curr]=max(result[curr],result[now]+time[curr])
      if(jinip[curr]==0):
        q.append(curr)

topology()
for i in range(n):
  print(result[i])