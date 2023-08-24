T = int(input())
for t in range(1, T + 1):
    N, K = map(int, input().split())
    MAP = [list(map(int, input().split()))for _ in range(N)]
    blank_row = [[] for _ in range(15)]
    blank_col = [[] for _ in range(15)]
    result = 0
    for i in range(N):
        count_row = 0
        count_col = 0
        for j in range(N):
            row = MAP[i][j]
            col = MAP[j][i]
            if row == 1:
                count_row += 1
            else:
                count_row = 0
            blank_row[i].append(count_row)
            if col == 1:
                count_col += 1
            else:
                count_col = 0
            blank_col[i].append(count_col)
    for i in blank_row:
        if len(i) > 0:
            result += i.count(K)
            if K+1 in i:
                result -= i.count(K+1)

    for i in blank_col:
        if len(i) > 0:
            result += i.count(K)
            if K+1 in i:
                result -= i.count(K+1)

    print(f'#{t} {result}')
