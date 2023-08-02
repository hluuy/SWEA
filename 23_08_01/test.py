# N = 2 # 행의 크기
# M = 4 # 열의 크기
# arr = [[0, 1, 2, 3], [4, 5, 6, 7]]
# 행 우선 순회
# for i in range(N):
#     for j in range(M):
#         print(arr[i][j])
# # 열 우선 순회
# for j in range(M):
#     for i in range(N):
#         print(arr[i][j])
# # 지그재그 순회
# for i in range(N):
#     for j in range(M):
#         print(arr[i][j + ( M - 1 - 2 * j ) * ( i % 2 )])

# arr = [[0]*M for _ in range(N)]
# arr2 = [[0]*M]*N # 참조하는 arr[i]만 만들어져 똑같은 값만을 참조하여 출력되는 값이 같다

# arr[0][0] = 1
# arr2[0][0] = 1
# print(arr)
# print(arr2)

# arr = [[0, 1, 2, 3], [4, 5, 6, 7]]
# max_v = 0
# for i in range(N):
#     row_total = 0
#     for j in range(M):
#         row_total += arr[i][j]
#     if max_v < row_total:
#         max_v = row_total
# print(max_v)

# arr[0...N-1][0...N-1] # N*N 배열
# di[] <- [0, 1, 0, -1]
# dj[] <- [1, 0, -1, 0]
# for i : #0 -> N-1
#     for j : #0 -> N-1
#         for k in range(4):
#             ni <- i + di[k]
#             nj <- j + dj[k]
#             if 0<=ni<N and 0<=nj<N

# '''
# 3
# 1 2 3
# 4 5 6
# 7 8 9
# '''
# di = [0, 1, 0, -1]
# dj = [1, 0, -1, 0]
# N = int(input())
# arr = [list(map(int, input().split()))for _ in range(N)]
#
# max_v = 0 # 모든 원소가 0 이상
# for i in range(N): # 모든 원소 arr[i][j]에 대해
#     for j in range(M):
#         #arr[i][j]을 중심으로
#         s = arr[i][j]
#         for k in range(4):
#             ni, nj = i + di[k], j + dj[k]
#             if 0<=ni<N and 0<=nj<N: # 배열을 벗어나지 않는다면
#                 s += arr[ni][nj]
#         # 여기까지 주변 원소를 포함한 합
#         if max_v < s:
#             max_v = s

# N = int(input())
# arr = [list(map(int, input().split()))for _ in range(N)]
#
# max_v = 0 # 모든 원소가 0 이상
# for i in range(N): # 모든 원소 arr[i][j]에 대해
#     for j in range(M):
#         #arr[i][j]을 중심으로
#         s = arr[i][j]
#         for di, dj in [[0. 1], [1, 0],[0, -1], [-1, 0]]:
#             ni, nj = i + di, j + dj
#             if 0<=ni<N and 0<=nj<N: # 배열을 벗어나지 않는다면
#                 s += arr[ni][nj]
#         # 여기까지 주변 원소를 포함한 합
#         if max_v < s:
#             max_v = s

# N = int(input())
# arr = [list(map(int, input().split()))for _ in range(N)]
#
# max_v = 0 # 모든 원소가 0 이상
# for i in range(N): # 모든 원소 arr[i][j]에 대해
#     for j in range(M):
#         #arr[i][j]을 중심으로
#         s = arr[i][j]
#         for k in range(4):
#             for p in range(1, m):
#             ni, nj = i + di[k]*p, j + dj[k] *p
#             if 0<=ni<N and 0<=nj<N: # 배열을 벗어나지 않는다면
#                 s += arr[ni][nj]
#         # 여기까지 주변 원소를 포함한 합
#         if max_v < s:
#             max_v = s

# i : 행의 좌표, len(arr)
# j : 열의 좌표, len(arr[0])
# arr = [[1,2,3],[4,5,6],[7,8,9]] # 3*3 행렬
#
# for i in range(3):
#     for j in range(3):
#         if i < j: # 오른쪽 위
#             arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
#         if j < i: # 왼쪽 아래
#

N = int(input())
arr = [list(map(int, input().split()))for _ in range(N)]
total1 = 0
total2 = 0
for i in range(N):
    total1 += arr[i][i]