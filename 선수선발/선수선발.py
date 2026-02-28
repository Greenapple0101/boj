T=int(input())
for tc in range(T):
    N,K=map(int,input().split())
    lst=list(map(int,input().split()))
    lst.sort()
    max_count=0
    left=0
    for right in range(N):
        while(lst[right]-lst[left]>K):
            left+=1

        current=right-left+1
        if(current>max_count):
            max_count=current
    print(f"#{tc+1} {max_count}", end="\n")

