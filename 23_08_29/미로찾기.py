def dfs(row, col):
    visited[row][col] = 1
    if MAP[row][col] == '3':
        return True
    for p in range(4):
        ni, nj = row + di[p], col + dj[p]
        if 0 <= ni < N and 0 <= nj < N:
            if not visited[ni][nj] and (MAP[ni][nj] == '0' or MAP[ni][nj] == '3'):
                if dfs(ni, nj):
                    return True
    return False


T = int(input())
for t in range(1, T + 1):
    N = int(input())
    MAP = [list(input())for _ in range(N)]
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    start_row = 0
    start_col = 0
    visited = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            a = MAP[i][j]
            if a == '2':
                start_row, start_col = i, j

    if dfs(start_row, start_col):
        result = 1
    else:
        result = 0
    print(f'#{t} {result}')