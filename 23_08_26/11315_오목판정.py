# # T = int(input())
# # for t in range(1, T + 1):
# #     N = int(input())
# #     MAP = [list(map(int, input().split()))for _ in range(N)]
# #     count = 0
# #     max_v = 0
# #     for i in range(N):
# #         for j in range(N):
# #             a = MAP[i][j]
# #             if ((N - 1) - i + 1) * ((N - 1) - j + 1) < max_v:
# #                 break
# #             for p in range(i, N):
# #                 for q in range(j, N):
# #                     s = MAP[p][q]
# #                     if a == s:
# #                         size = (p - i + 1) * (q - j + 1)
# #                         if max_v < size:
# #                             max_v = size
# #                             count = 1
# #                         elif max_v == size:
# #                             count += 1
# #     print(f'#{t} {count}')
# def row(i, j):
#     global count
#     if count >= 5:
#         result.append(1)
#         return
#     if 0 < j + 1 < N:
#         if OMOK[i][j + 1] == 'o':
#             count += 1
#             row(i, j + 1)
#
#
# def col(i, j):
#     global count
#     if count >= 5:
#         result.append(1)
#         return
#     if 0 < i + 1 < N:
#         if OMOK[i + 1][j] == 'o':
#             count += 1
#             col(i + 1, j)
#
#
# def X1(i, j):
#     global count
#     if count >= 5:
#         result.append(1)
#         return
#     if 0 < i + 1 < N and 0 < j + 1 < N:
#         if OMOK[i + 1][j + 1] == 'o':
#             count += 1
#             X1(i + 1, j + 1)
#
#
# def X2(i, j):
#     global count
#     if count >= 5:
#         result.append(1)
#         return
#     if 0 < i + 1 < N and 0 <= j - 1 < N:
#         if OMOK[i + 1][j - 1] == 'o':
#             count += 1
#             X2(i + 1, j - 1)
#
#
# T = int(input())
# for t in range(1, T + 1):
#     N = int(input())
#     OMOK = [list(input()) for _ in range(N)]
#     count = 0
#     result = []
#     for i in range(N):
#         for j in range(N):
#             a = OMOK[i][j]
#             if a == 'o':
#                 count = 1
#                 row(i, j)
#                 count = 1
#                 col(i, j)
#                 count = 1
#                 X1(i, j)
#                 count = 1
#                 X2(i, j)
#     if result:
#         print('yes')
#     else:
#         print('no')
def row(i, j):
    global count
    if count >= 5:
        result.append(1)
        return
    if 0 < j + 1 < N:
        if OMOK[i][j + 1] == 'o':
            count += 1
            row(i, j + 1)


def col(i, j):
    global count
    if count >= 5:
        result.append(1)
        return
    if 0 < i + 1 < N:
        if OMOK[i + 1][j] == 'o':
            count += 1
            col(i + 1, j)


def X1(i, j):
    global count
    if count >= 5:
        result.append(1)
        return
    if 0 < i + 1 < N and 0 < j + 1 < N:
        if OMOK[i + 1][j + 1] == 'o':
            count += 1
            X1(i + 1, j + 1)


def X2(i, j):
    global count
    if count >= 5:
        result.append(1)
        return
    if 0 < i + 1 < N and 0 <= j - 1 < N:
        if OMOK[i + 1][j - 1] == 'o':
            count += 1
            X2(i + 1, j - 1)


T = int(input())
for t in range(1, T + 1):
    N = int(input())
    OMOK = [list(input()) for _ in range(N)]
    count = 0
    result = []
    for i in range(N):
        for j in range(N):
            a = OMOK[i][j]
            if a == 'o':
                count = 1
                row(i, j)
                count = 1
                col(i, j)
                count = 1
                X1(i, j)
                count = 1
                X2(i, j)
    if result:
        print(f'#{t}','YES')
    else:
        print(f'#{t}','NO')