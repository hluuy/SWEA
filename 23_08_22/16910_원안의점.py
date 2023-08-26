T = int(input())
for t in range(1, T + 1):
    N = int(input())
    count = 0
    for i in range(1, N):
        for j in range(1, N):
            if (i * i) + (j * j) <= (N * N):
                count += 1
    result = (count + N) * 4 + 1
    print(f'#{t} {result}')
