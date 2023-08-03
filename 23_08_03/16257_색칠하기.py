T = int(input())
for t in range(1, T + 1):
    N = int(input())
    lst = [list(map(int, input().split()))for _ in range(N)]
    M = 10
    a = [[0]*10 for _ in range(10)]
    fold = 0
    wanted = 3

    for q in range(N):
        x1 = lst[q][0]
        y1 = lst[q][1]
        x2 = lst[q][2]
        y2 = lst[q][3]
        c = lst[q][4]
        for i in range(x1, x2+1):
            for j in range(y1, y2+1):
                if c == 1:
                    a[i][j] += 1
                else:
                    a[i][j] += 2
    for p in range(M):
        for q in range(M):
            if a[p][q] == 3:
                fold += 1


    print(f'#{t} {fold}')
