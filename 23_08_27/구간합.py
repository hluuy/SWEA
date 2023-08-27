T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))
    max_v = 0
    min_v = 999999999
    for i in range(N):
        if i + M < N + 1:
            if sum(lst[i : i + M]) < min_v:
                min_v = sum(lst[i : i + M])
            if sum(lst[i : i + M]) > max_v:
                max_v = sum(lst[i : i + M])

    result = max_v - min_v
    print(f'#{t} {result}')
