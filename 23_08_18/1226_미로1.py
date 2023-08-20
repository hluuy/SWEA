def bfs(row, col, N):
    visited = [[0]*N for _ in range(N)] # visited 생성
    Q = [] # 큐 생성
    di = [0, 1, 0, -1]      # 탐색을 위한 범위 지정
    dj = [1, 0, -1, 0]
    Q.append((row, col))    # 시작점 enq
    visited[row][col] = 1   # 시작점 도달표시
    while Q:                # 큐가 비워질 때 까지
        i, j = Q.pop(0)     # deq
        if MAP[i][j] == 3:  # 처리
            return 1        # 도착했을 때 리턴 값
        for p in range(4):
            ni, nj = i+di[p], j+dj[p]
            if 0 <= ni < N and 0 <= nj < N and MAP[ni][nj] != 1 and visited[ni][nj] == 0 :
                Q.append((ni, nj))
                visited[ni][nj] = visited[i][j]
    return 0                # 3인 칸에 도달할 수 없는 경우

for _ in range(1, 11):
    t = int(input())
    MAP = [list(map(int,input()))for _ in range(16)]
    for i in range(16): # 시작점 찾기, 함수로 만드는거랑 뭐가 다른가,,,?
        for j in range(16):
            if MAP[i][j] == 2:
                s_row, s_col = i, j
    ans = bfs(s_row, s_col, 16)

    print(f'#{t} {ans}')

# def bfs(row, col, N):
#     visited = [[0]*N for _ in range(N)] # visited 생성
#     Q = [] # 큐 생성
#     di = [0, 1, 0 ,-1]      # 탐색을 위한 범위 지정
#     dj = [1, 0 ,-1, 0]
#     Q.append((row, col))    # 시작점 enq
#     visited[row][col] = 1   # 시작점 도달표시
#     while Q:                # 큐가 비워질 때 까지
#         i, j = Q.pop(0)     # deq
#         if MAP[i][j] == 3:  # 처리
#             return 1        # 도착했을 때 리턴 값
#         # 인접하고 enq된 적이 없으면
#         # enq, enq표시는 어떻게?
#         for p in range(4):
#             ni, nj = i+di[p], j+dj[p]
#             if 0 <= ni < N and 0 <= nj < N and MAP[ni][nj] != 1 and visited[ni][nj] == 0 :
#                 Q.append((ni, nj))
#                 visited[ni][nj] = visited[i][j]
#     return 0                # 3인 칸에 도달할 수 없는 경우
#
#
# T = 10
# for _ in range(1, T + 1):
#     t = int(input())
#     MAP = [list(map(int,input()))for _ in range(16)]
#
#     row = 0
#     col = 0
#     # g_row = 0 # 도착점도 찾아야하나,,,?
#     # g_col = 0 # 필요없다
#     for i in range(16): # 시작점 찾기, 함수로 만드는거랑 뭐가 다른가,,,?
#         for j in range(16):
#             if MAP[i][j] == 2:
#                 row, col = i, j
#             # if MAP[i][j] == 3:
#             #     g_row, g_col = i, j
#
#     ans = bfs(row, col, 16)
#     print(f'#{t} {ans}')
#
