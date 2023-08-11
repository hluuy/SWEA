def sudoku(arr):
    for i in range(9):
        cnt = [0] * 10
        for j in range(9):
            cnt[arr[i][j]] += 1
        for k in range(1, 10):
            if cnt[k] == 0:  # 1~9 사이에 빠진 숫자가 있으면
                return 0  # 0 리턴


T = int(input())
for t in range(1, T + 1):
    arr = [list(map(int, input().split()))for _ in range(9)]



    ans = sudoku(arr)  #스도쿠가 완성되면 1, 아니면 0
    print(f'#{t} {ans}')
    # for i in range(9):
    #     cnt = [0] * 10
    #     for j in range(9):
    #         cnt[arr[i][j]] += 1
    #     for k in range(1, 10):
    #         if cnt[k] == 0:  # 1~9 사이에 빠진 숫자가 있으면
    #             ans = 0
    #             break  # for k 탈출
    #
    #     if ans == 0:
    #         break