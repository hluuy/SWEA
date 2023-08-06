T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    lst = [list(map(int, input().split()))for _ in range(N)]
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    dp = [-1, 1, 1, -1]
    dq = [1, 1, -1, -1]
    max_v = 0
    max_a = 0
    max_b = 0
    for i in range(N):
        for j in range(N):
            a = lst[i][j]
            for p in range(4):
                for q in range(1, M):
                    ni, nj = i + di[p]*q, j + dj[p]*q
                    if 0<= ni < N and 0 <= nj < N:
                        a += lst[ni][nj]

            if max_a < a:
                max_a = a

    for i in range(N):
        for j in range(N):
            b = lst[i][j]
            for p in range(4):
                for q in range(1, M):
                    ni, nj = i + dp[p]*q, j + dq[p]*q
                    if 0 <= ni < N and 0 <= nj < N:
                        b += lst[ni][nj]

            if max_b < b:
                max_b = b

    if max_a > max_b:
        max_v = max_a
    elif max_b > max_a:
        max_v = max_b

    print(f'#{t} {max_v}')