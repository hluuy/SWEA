T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    lst = [input()for _ in range(N)]
    result = ''
    for i in range(N):
        for p in range(N - M + 1):
            if 0 <= p < N - M + 1:
                if [lst[i][p], lst[i][p + 1], lst[i][p + 2], lst[i][p + 3]] == [lst[i][p + M - 1], lst[i][p + M - 2], lst[i][p + M - 3], lst[i][p + M - 4]]:
                    result += lst[i][p:p + M]

    for j in range(N):
        for q in range(N - M + 1):
            if 0 <= q < N - M + 1:
                if [lst[q][j], lst[q + 1][j], lst[q + 2][j], lst[q + 3][j]] == [lst[q + M - 1][j], lst[q + M - 2][j], lst[q + M - 3][j], lst[q + M - 4][j]]:
                    for c in range(q, q + M):
                        result += lst[c][j]

    print(f'#{t} {result}')