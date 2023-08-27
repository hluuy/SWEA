T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    MAP = [list(map(int, input().split()))for _ in range(N)]
    max_v = 0
    for i in range(N):
        for j in range(N):
            s = 0
            for p in range(M):
                for q in range(M):
                    ni, nj = i + p, j + q
                    if 0 <= ni < N and 0 <= nj < N:
                        s += MAP[ni][nj]

            if max_v < s:
                max_v = s
    print(f'#{t} {max_v}')
