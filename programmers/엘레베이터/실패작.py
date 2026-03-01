def solution(n,calls):
    answer=[0]*len(calls)
    to_visit=[]
    check=1
    ##1 올라가는거, -1은 내려가는거
    for i in range(len(calls)):
        to_visit.append(calls[i][1])
        to_visit.sort()
        if (to_visit == []): continue
        if(i==0):
            answer[i]=1
        elif(i==1):
            if(calls[i][0]-calls[i-1][0]+1>to_visit[-1]):
                answer[i]=to_visit[-1]
                del to_visit[-1]
                if(answer[i]<calls[i][1]):
                    check=1
                else:
                    check=-1
            else:
                answer[i]=calls[i][0] - calls[i - 1][0] + 1
        else:
            if(check==1 and answer[i-1]+calls[i][0]-calls[i-1][0]>to_visit[-1]):
                answer[i]=to_visit[-1]
                l=answer[i-1]+calls[i][0]-calls[i-1][0]-to_visit[-1]
                del to_visit[-1]
                if (answer[i] < calls[i][1]):
                    check = 1
                else:
                    check = -1
                print("1")
            elif(check==1 and answer[i-1]+calls[i][0]-calls[i-1][0]<=to_visit[-1]):
                answer[i]=answer[i - 1] + calls[i][0] - calls[i - 1][0]
                print("2")
            elif (check == -1 and answer[i - 1] - (calls[i][0] - calls[i - 1][0]) < to_visit[0]):
                answer[i] = to_visit[0]
                del to_visit[0]
                if (answer[i] < calls[i][1]):
                    check = 1
                else:
                    check = -1
                print("3")
            elif (check == -1 and answer[i - 1] - (calls[i][0] - calls[i - 1][0]) >= to_visit[0]):
                answer[i] = answer[i - 1] - (calls[i][0] - calls[i - 1][0])
                print("4")
    return answer

print(solution(8,[[1, 5], [7, 2], [8, 5]]))
print(solution(1000,[[3, 500], [505, 400], [606,600], [607, 400], [608, 500]]))
print(solution(90,[[11, 50], [20, 1], [60, 90], [61,2]]))
print(solution(20,[[1, 10], [5, 3], [6, 7], [11, 7],[100, 1]]))

## 다하고 나서 마지막 테케에서 걸리는 걸 깨달음