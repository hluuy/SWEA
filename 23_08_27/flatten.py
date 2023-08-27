T = 10
for t in range(1, T + 1):
    N = int(input())
    MAP = list(map(int, input().split()))
    count = 0
    while count < N:
        MAP.sort()
        max_v = MAP.pop()
        min_v = MAP.pop(0)
        MAP.append(max_v - 1)
        MAP.append(min_v + 1)
        count += 1
    result = max(MAP) - min(MAP)
    print(f'#{t} {result}')
