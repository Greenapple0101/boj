def solution(n, costs):
    #비용순 정렬
    costs.sort(key=lambda x:x[2])
    
    parent=[i for i in range(n)]
    
    #재귀라서 계속 타고 올라감, 만약 자기가 루트가 아니면 부모 찾기
    def find(x):
        if parent[x]!=x:
            parent[x]=find(parent[x])
        return parent[x]
    
    #트리 합치기 a,b 순서 상관없음
    #a부모 찾고 b부모 찾아서 한 트리 밑으로 다른 트리 집어넣는거
    #원래 순서대로 정렬되어있던 parent 배열이 변함
    def union(a,b):
        root_a=find(a)
        root_b=find(b)
        
        if root_a==root_b:
            return False
        
        parent[root_a]=root_b
        return True
    
    answer = 0
    count = 0
    
    #성공한 연결이 섬개수-1 이 되면 섬이 다 연결된것
    #만약 두 섬의 루트가 다르면 그 둘을 연결시킨후에 비용더하기
    #앞에서 비용 순대로 정렬한게 핵심. 싼비용부터 보기때문에
    #최소신장트리를 만들고 최적비용해가 구해짐
    for a,b,cost in costs:
        if union(a,b):
            answer += cost
            count += 1
            
            if count == n-1:
                break
    
    return answer