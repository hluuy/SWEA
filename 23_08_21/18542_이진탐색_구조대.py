def traversal(v):
    global value
    if v <= N:
        traversal(v * 2)
        lst[v] = value
        value += 1
        traversal(v * 2 + 1)

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    lst = [0] * (N + 1)
    value = 1
    traversal(1)

    print(f'#{t}',lst[1], lst[N // 2])