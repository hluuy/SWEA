T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    lst = [list(map(int, input().split()))for _ in range(N)]
    max_v = 0
    for i in range(N):
        for j in range(N):
            # a = lst[i][j]
            s = 0
            for k in range(M):
                for z in range(M):
                    ni = i+k
                    nj = j+z
                    if 0<= ni < N and 0<= nj < N:
                        s += lst[ni][nj]

            if max_v < s:
                max_v = s
    print(f'#{t} {max_v}')
