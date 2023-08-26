T = 10
for t in range(1, T + 1):
    N = int(input())
    MAP = [list(map(int, input().split()))for _ in range(N)]
    lst = [[] for _ in range(N)]
    col_lst= []
    count = 0
    for i in range(N):
        for j in range(N):
            a = MAP[j][i]
            if not a == 0:
                lst[i].append(a)
    for item in lst:
        for i in range(len(item)):
            if 1 <= i and item[i] == 2 and item[i-1] == 1:
                i += 1
                count += 1
            # if item[i-1] == 1:
            # lst[i].append(a)
            # for item in lst:
            #     for p in item:
            #         if p != 0:
            #             col_lst[i].append(p)

    print(f'#{t} {count}')
    # result = 0
    # i = 0
    # while i < len(col_lst) - 1:
    #     if col_lst[i] == 1 and col_lst[i + 1] == 2:
    #         result += 1
    #         i += 2
    #     else:
    #         i += 1
    # print(result)
    # result = [[] for _ in range(len(col_lst) - 1)]
    # for i in range(len(col_lst)):
    #     if i < len(col_lst) - 1:
    #         result[i].append(col_lst[i])
    #         result[i].append(col_lst[i + 1])
    # print(result.count([1, 2]))
    # i = 0
    # while i < len(col_lst) - 1:
    #     if col_lst[i] == 1 and col_lst[i + 1] == 2:
    # # for i in range(len(col_lst)):
    # #     if i < len(col_lst) - 1:
    # #         if col_lst[i] == 1:
    # #             if col_lst[i+1] == 2:
    #         col_lst.pop(i)
    #         col_lst.pop(i)
    #         count += 1
    #     else:
    #         i += 1
    # for i in range(len(col_lst)):
    #     if i < len(col_lst) - 1:
    #         if col_lst[i] == 1 and col_lst[i + 1] == 2:
    #             col_lst.pop(i)
    #             col_lst.pop(i)
    #             count += 1





# def run(row, col):
#     a = MAP[row][col]
#     if a == 1:
#         while row < N - 1:
#             row += 1
#             s = MAP[row][col]
#             if s == 2:
#                 MAP[row][col] = 0
#                 MAP[row - 1][col] = 0
#                 return 1
#     else:
#         if row < N - 1:
#             row += 1
#             run(row, col)
#     return 0
#
# T = 10
# for t in range(1, T + 1):
#     N = int(input())
#     MAP = [list(map(int, input().split()))for _ in range(100)]
#     count = 0
#     for i in range(N):
#         for j in range(N):
#             count += run(i, j)
#             # 함수로 만들자
#             # if a == 1:
#             #     while True:
#             #         s = MAP[i][j]
#             #         if s == 2:
#             #             MAP.pop(a)
#             #             MAP.pop(s)
#             #             count += 1
#             #             break
#             #         else:
#             #             continue
#             #         if i < N - 1 :
#             #             i += 1
#             #     break
#     print(count)