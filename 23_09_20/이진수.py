T = int(input())
for t in range(1, T + 1):
    N, N16 = input().split()
    num = int(N16, 16)

    result = bin(num)[2:]
    if len(result) % 4 != 0:
        result = '0' + result

    print(f'#{t} {result}')
