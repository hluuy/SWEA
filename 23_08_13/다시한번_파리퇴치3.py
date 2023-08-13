T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    lst = [list(map(int, input().split()))for _ in range(N)]
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    dp = [-1, 1, 1, -1]
    dq = [1, 1, -1, -1]
    max_v = 0
    max_t = 0
    max_x = 0
    for i in range(N):
        for j in range(N):
            a = lst[i][j]
            t = 0
            for p in range(4):
                for q in range(1, M):
                    ni, nj = i+di[p]*q, j+dj[p]*q
                    if 0<= ni < N and 0 <= nj < N:
                        t += lst[ni][nj]

            if max_t < a+t:
                max_t = a+t
            x = 0
            for p in range(4):
                for q in range(1, M):
                    ni, nj = i+dp[p]*q, j+dq[p]*q
                    if 0 <= ni < N and 0 <= nj < N:
                        x += lst[ni][nj]

            if max_x < a+x:
                max_x = a+x
    if max_t > max_x:
        max_v = max_t
    elif max_x > max_t:
        max_v = max_x

    print(f'#{tc} {max_v}')
