# #오목판정
# - 한 줄씩만 순회?
#     -> row 값만 증가시키면서 탐색 'o'가 5개 이상이면 yes
#     -> col 값만 증가시키면서 탐색 'o'가 5개 이상이면 yes
#     -> 대각은?
#         -> 결국 대각을 순회하는 델타를 만들어야 하나?
#     -> 만약 돌이 8개가 연속으로 있을 때, 1번째 'o'도 인식, 2번째 'o'도 인식하면 어떻게?
#         -> 5개 이상인 개수를 세는 것이 아닌 현재 오목판 위에 있냐/없냐를 물어보기에 상관없음
#     -> 결국 OMOK[i][j]에서 j값만 += 1 하며 늘어나는데 'o'를 만나면 count += 1
#         '.'을 만나면 count는 0으로 초기화
#         이때, count가 5 이상이 된다면 yes
#     -> 그럼 열 순회, 행 순회, 대각 순회하는 함수를 각각 만들어야 하나?
#     how can i do that?
#     -> 함수 호출 할 때 어떤 값을 넣어서 호출을 해야하지?
#     -> 필요한게 뭐지? i, j 값?

def row(i, j):
    global count
    if count >= 5:
        return 1
    if 0 < j + 1 < N:
        if OMOK[i][j + 1] == 'o':
            count += 1
            row(i, j + 1)


def col(i, j):
    global count
    if count >= 5:
        return 1
    if 0 < i + 1 < N:
        if OMOK[i + 1][j] == 'o':
            count += 1
            col(i + 1, j)


def X1(i, j):
    global count
    if count >= 5:
        return 1
    if 0 < i + 1 < N and 0 < j + 1 < N:
        if OMOK[i + 1][j + 1] == 'o':
            count += 1
            X1(i + 1, j + 1)


def X2(i, j):
    global count
    if count >= 5:
        return 1
    if 0 < i + 1 < N and 0 < j - 1 < N:
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
                result.append(row(i, j))
                result.append(col(i, j))
                result.append(X1(i, j))
                result.append(X2(i, j))

    if 1 not in result:
        print('no')
    else:
        print('yes')


