from collections import deque

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        g=[[] for _ in range(numCourses)]
        indegree=[0]*numCourses
        #각 배열에 b를 선수과목으로 필요로하는 과목들을 넣는다
        #그리고 a의 진입차수를 1개씩 늘린다
        for a,b in prerequisites:
            g[b].append(a)
            indegree[a]+=1

        q=deque()

        #만약 i의 진입차수가 0이면, 즉 i가 필요한 선수과목이 하나도 없으면ㅌ
        #큐에 i넣기
        for i in range(numCourses):
            if indegree[i]==0:
                q.append(i)
        
        count=0
        #큐가 다 빌때까지 큐에서 진입차수 0인 과목 쫓아내고
        #카운트 1세기
        #그리고 큐밖으로 쫓아낸 과목을 선수과목으로 필요로하는 과목들 흝기
        #그 과목들의 진입차수 하나 깎기
        #그리고 그 과목의 진입차수가 0일경우 큐에 넣고 다시 도돌이표
        #사이클이 생기면 진입차수가 0인 과목이 더 생기지 않아서 카운트가 과목수보다 작게 끝남
        while q:
            q1=q.popleft()
            count+=1
            for nxt in g[q1]:
                indegree[nxt]-=1
                if indegree[nxt]==0:
                    q.append(nxt)
        #만약 카운트랑 과목수랑 같으면 true 리턴. 왜 카운트랑 과목수랑 같아야하는가. 사이클이 없다는걸 보여주는거
        return count==numCourses
