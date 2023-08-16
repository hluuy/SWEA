# 미로찾기
# 2에서 출발하여 3에 도착하는,,, 벽은 1, 통로는 0
# 먼저 MAP을 순회하며 2나 3의 좌표를 찾고
# 해당 좌표에서부터 시작?
# 만약 2의 좌표를 찾았다면 그 좌표를 시작으로 델타 돌려서 0이 있으면 움직이도록?
# 만약 가다가 벽에 막히면 돌아와야하니까 스택에 담아둬야하나?
# dfs 문제 풀었던 것처럼 그냥 함수로 돌리면 되려나?
# dfs 문제처럼 풀려면 간선 정보를 어떻게 담아야하지?
# 델타탐색 돌리면 되려나?


def dfs(x, y):
    visited[x][y] = True
    if MAP[x][y] == 3:
        return True
    for p in range(4):
        ni, nj = x + di[p], y + dj[p]
        if 0 <= ni < N and 0 <= nj < N:
            if not visited[ni][nj] and (MAP[ni][nj] == 0 or MAP[ni][nj] == 3):
                if dfs(ni, nj):
                    return True
    return False

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    MAP = [list(map(int, input()))for _ in range(N)]
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    start_x = 0
    start_y = 0
    end_x, end_y = 0, 0
    for i in range(N):
        for j in range(N):
            if MAP[i][j] == 2:
                start_x, start_y = i, j

    visited = [[False] * N for _ in range(N)]

    if dfs(start_x, start_y):
        result = 1
    else:
        result = 0

    print(f'#{t} {result}')
