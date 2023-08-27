T = int(input())
for t in range(1, T + 1):
    N = int(input())
    MAP = [list(map(int, input().split()))for _ in range(N)]
    max_size = 0
    count = 0
    for i in range(N):
        for j in range(N):
            a = MAP[i][j]
            if (N - i + 1) * (N - j + 1) < max_size:
                break
            for p in range(N):
                for q in range(N):
                    s = MAP[p][q]
                    if a == s:
                        if max_size < (p - i + 1) * (q - j + 1):
                            max_size = (p - i + 1) * (q - j + 1)
                            count = 1
                        elif max_size == (p - i + 1) * (q - j + 1):
                            count += 1
    print(f'#{t} {count}')