T = 10
for t in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    gap = 0
    min_v = 0
    max_v = 0
    i = 0
    for _ in range(N):
        lst.sort()
        min_v = lst[0] + 1
        max_v = lst[99] - 1
        lst[0] = min_v
        lst[99] = max_v
        i += 1
        if i == N:
            lst.sort()
            min_v = lst[0]
            max_v = lst[99]
            gap = max_v - min_v

    print(f'#{t} {gap}')