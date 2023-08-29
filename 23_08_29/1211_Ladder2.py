# def dfs(row, col, count):
#     visited[row][col] = 1
#     if row == 99:
#         return count
#     if 0 < col < 99:
#         if MAP[row][col - 1] or MAP[row][col + 1] == 1:
#             for p in range(2):
#                 ni, nj = row + di[p], col + dj[p]
#                 if 0 <= ni < 100 and 0 <= nj < 100:
#                     if not visited[ni][nj] and MAP[ni][nj] == 1:
#                         if dfs(ni, nj, count+1):
#                             return True
#         else:
#             ni, nj = row + 1, col
#             if 0 <= ni < 100 and 0 <= nj < 100:
#                 if not visited[ni][nj] and MAP[ni][nj] == 1:
#                     if dfs(ni, nj, count+1):
#                         return True
#     return False
def dfs(row, col, count):
    visited[row][col] = 1

    if row == 99:
        return count
    if col < 99 and MAP[row][col + 1] == 1 and not visited[row][col + 1]:
        return dfs(row, col + 1, count + 1)
    elif col > 0 and MAP[row][col - 1] == 1 and not visited[row][col - 1]:
        return dfs(row, col - 1, count + 1)
    elif row < 99 and MAP[row + 1][col] == 1 and not visited[row + 1][col]:
        return dfs(row + 1, col, count + 1)

    return False


T = 10
for t in range(1, T + 1):
    input()
    MAP = [list(map(int, input().split()))for _ in range(100)]
    result = 99999999
    result_col = 0
    for i in range(100):
        visited = [[0] * 100 for _ in range(100)]
        if MAP[0][i] == 1:
            min_v = dfs(0, i, 0)
            if result > min_v:
                result = min_v
                result_col = i
    print(f'#{t} {result_col}')
