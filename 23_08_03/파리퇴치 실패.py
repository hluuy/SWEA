T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(N)]
    di = [0, 1, 1]
    dj = [1, 1, 0]
    max_v = 0

    for i in range(N):
        for j in range(N):
            a = lst[i][j]
            for k in range(3):
                for z in range(1, M):
                    ni, nj = i + (di[k] * z), j + (dj[k] * z)
                    if 0 <= ni < N and 0 <= nj < N:
                        a += lst[ni][nj]
            if M > 2:
                ni, nj = (N-M) // 2 + 1 , j + 1
                if i < nj < M:
                    a += lst[ni][nj]
            if M > 2:
                ni, nj = i + 1, (N-M) // 2 + 1
                if i< ni < M:
                    a += lst[ni][nj]
            # if max_v < a:
            #     max_v = a



        # if M > 2:
        #     for i in range(N):
        #         for j in range(N):
        #             ni, nj = M - i, j + 1
        #             if 1 < nj < M:
        #                 a += lst[ni][nj]
        #     for j in range(N):
        #         for i in range(N):
        #             ni, nj = i + 1, M - j
        #             if 1 < ni < M:
        #                 a += lst[ni][nj]


            if max_v < a:
                max_v = a

    print(max_v)
