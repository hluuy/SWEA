def game(i, j, bw, N):
    board[i][j] = bw
    for di, dj in [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]:
        ni, nj = i + di, j + dj

        tmp = []
        while 0 <= ni < N and 0 <= nj < N and board[ni][nj] == opc[bw]:
            tmp.append((ni, nj))
            ni, nj = ni+di, nj+dj
        if 0 <= ni < N and 0 <= nj < N and board[ni][nj] == bw:
            for p, q in tmp:
                board[p][q] = bw

B = 1
W = 2
opc = [0, 2, 1]

T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    play = [list(map(int, input().split()))for _ in range(M)]
    board = [[0]*N for _ in range(N)]
    board[N // 2 - 1][N // 2 - 1] = W
    board[N // 2 - 1][N // 2] = B
    board[N // 2][N // 2 - 1] = B
    board[N // 2][ N // 2] = W
    for col, row, bw in play:
        game(row-1, col-1, bw, N)
    bcnt = wcnt = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == B:
                bcnt += 1
            elif board[i][j] == W:
                wcnt += 1
    print(f'#{t} {bcnt} {wcnt}')