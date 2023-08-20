def bfs(row, col, N):
    visited = [[0] * N for _ in range(N)]
    Q = []
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    visited[row][col] = 1
    Q.append((row, col))
    while Q:
        i, j = Q.pop(0)
        if MAP[i][j] == 3:
            return 1
        for p in range(4):
            ni, nj = i + di[p], j + dj[p]
            if 0 <= ni < N and 0 <= nj < N and MAP[ni][nj] != 1 and visited[ni][nj] == 0:
                Q.append((ni, nj))
                visited[ni][nj] = visited[i][j]
    return 0

T = 10
for _ in range(1, T + 1):
    t = int(input())
    MAP = [list(map(int, input())) for _ in range(16)]
    for i in range(16):
        for j in range(16):
            if MAP[i][j] == 2:
                s_row, s_col =i, j
    ans = bfs(s_row, s_col, 16)

    print(f'#{t} {ans}')
