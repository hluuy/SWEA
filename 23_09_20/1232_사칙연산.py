T = 10
for t in range(1, T + 1):
    N = int(input())
    tree = [list(input().split()) for _ in range(N)]
    tree = [0] + tree

    for i in range(N, 0, -1):
        if tree[i][1] in '+-*/':
            if tree[i][1] == '-':
                tree[i] = (i, int(tree[int(tree[i][2])][1]) - int(tree[int(tree[i][3])][1]))
            elif tree[i][1] == '*':
                tree[i] = (i, int(tree[int(tree[i][2])][1]) * int(tree[int(tree[i][3])][1]))
            elif tree[i][1] == '/':
                tree[i] = (i, int(tree[int(tree[i][2])][1]) / int(tree[int(tree[i][3])][1]))
            else:
                tree[i] = (i, int(tree[int(tree[i][2])][1]) + int(tree[int(tree[i][3])][1]))

    result = int(tree[1][1])

    print(f'#{t} {result}')
