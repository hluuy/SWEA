T = 10
for t in range(1, T + 1):
    N = int(input())
    lst = [input()for _ in range(8)]
    count = 0

    for i in range(8):
        for p in range(8 - N + 1):
            if 0 <= p < 8 - N + 1:
                if (lst[i][p], lst[i][p + 1], lst[i][p + 2]) == (lst[i][p + N-1], lst[i][p + N - 2], lst[i][p + N - 3]):
                    count += 1
    for j in range(8):
        for q in range(8 - N + 1):
            if 0 <= q < 8 - N + 1:
                if (lst[q][j], lst[q+1][j], lst[q+2][j]) == (lst[q + N-1][j], lst[q + N - 2][j], lst[q+N - 3][j]):
                    count += 1

    print(f'#{t} {count}')

    # for i in range(8):
    #     for p in range(8 - N + 1):
    #         if (lst[i][p], lst[i][p + 1]) == (lst[i][p + N - 1], lst[i][p + N - 2]):
    #             count += 1
    # for j in range(8):
    #     for q in range(8 - N + 1):
    #         if (lst[q][j], lst[q+1][j]) == (lst[q+ N - 1][j], lst[q+N - 2][j]):
    #             count += 1
