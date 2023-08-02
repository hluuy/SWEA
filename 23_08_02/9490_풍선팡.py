T = int(input())
for t in range(1, T+1):
    N, M = list(map(int, input().split())) # N = 행, M = 열
    lst = [list(map(int, input().split()))for _ in range(N)]
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    max_v = 0
    for i in range(N):
        for j in range(M):
            s = lst[i][j]
            a = 0
            for k in range(4):
                for z in range(1, s+1):
                    ni, nj = i + di[k]*z, j + dj[k]*z
                    if 0 <= ni < N and 0 <= nj <M:
                        a += lst[ni][nj]

            if max_v < a+s:
                max_v = a+s
    print(f'#{t} {max_v}')


