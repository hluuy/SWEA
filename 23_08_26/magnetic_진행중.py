def run(row, col):
    a = MAP[row][col]
    cnt = 0
    if a == 1:
        while row < N - 1:
            row += 1
            s = MAP[row][col]
            if s == 2:
                MAP[row][col] = 0
                MAP[row - 1][col] = 0
                cnt += 1
                return cnt
    else:
        if row < N - 1:
            row += 1
            run(row, col)
    run(row, col)

T = 10
for t in range(1, T + 1):
    N = int(input())
    MAP = [list(map(int, input().split()))for _ in range(100)]
    count = 0
    for i in range(N):
        for j in range(N):
            count += run(i, j)
            # 함수로 만들자
            # a = MAP[i][j]
            # if a == 1:
            #     while True:
            #         s = MAP[i][j]
            #         if s == 2:
            #             MAP.pop(a)
            #             MAP.pop(s)
            #             count += 1
            #             break
            #         else:
            #             continue
            #         if i < N - 1 :
            #             i += 1
            #     break
    print(count)