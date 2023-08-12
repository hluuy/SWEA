T = int(input())
for t in range(1 , T + 1):
    N, M = map(int, input().split())
    lst = [list(map(int, input().split()))for _ in range(N)]
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    max_v = 0
    for i in range(N):
        for j in range(M):
            a = lst[i][j]
            s = 0
            for p in range(4):
                ni, nj = i + di[p], j + dj[p]
                if 0 <= ni < N and 0 <= nj < M:
                    s += lst[ni][nj]
            if max_v < a+s:
                max_v = a + s

    print(f'#{t} {max_v}')
