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
            return visited[i][j] - 2
        for p in range(4):
            ni, nj = i + di[p], j + dj[p]
            if 0 <= ni < N and 0 <= nj < N and MAP[ni][nj] != 1 and visited[ni][nj] == 0:
                Q.append((ni,nj))
                visited[ni][nj] = visited[i][j] + 1
    return 0

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    MAP = [list(map(int, input()))for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if MAP[i][j] == 2:
                s_row, s_col = i, j
    ans = bfs(s_row, s_col, N)

    print(f'#{t} {ans}')
