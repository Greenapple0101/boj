T = int(input())

for tc in range(1, T+1):
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]
    check = [[0]*N for _ in range(N)]  # 술래가 둘일 경우 겹치는 감시구역을 빼야합니다
    wall = []
    man = []
    for i in range(N):  # 술래랑 벽 좌표 넣기
        for j in range(N):
            if (grid[i][j] == 1):
                wall.append([i, j])
            if (grid[i][j] == 2):
                man.append([i, j])

    dy = [0, 0, 1, -1]
    dx = [1, -1, 0, 0]
    grid1 = list(zip(*grid))  # 세로로 세기 위해
    count = 0  # 바깥에 선언해야합니다
    for val in man:
        i = val[0]
        row = grid[i]
        k = val[1]
        while (1):
            k += 1
            if (k >= N):
                break
            if (check[i][k]):
                continue
            if (row[k] == 1):
                break
            if(row[k]==0):count += 1
            check[i][k] = 1
        k = val[1]
        while (1):
            k -= 1
            if (k < 0):
                break
            if (check[i][k]):
                continue
            if (row[k] == 1):
                break
            if(row[k]==0):count += 1
            check[i][k] = 1

    for val in man:
        i = val[1]
        row = grid1[i]

        k = val[0]

        while (1):
            k += 1
            if (k >= N):
                break
            if (check[k][i]):
                continue
            if (row[k] == 1):
                break
            if(row[k]==0):count += 1
            check[k][i] = 1
        k = val[0]

        while (1):
            k -= 1
            if (k < 0):
                break
            if (check[k][i]):
                continue
            if (row[k] == 1):
                break
            if(row[k]==0):count += 1
            check[k][i] = 1

    ans = (N*N)-len(wall)-count-len(man)

    print(f"#{tc} {ans}")