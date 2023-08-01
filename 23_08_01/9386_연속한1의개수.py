T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = list(map(int, input()))
    count = 0
    max_c = 0
    result = 0
    for i in arr:
        if i == 1:
            count += 1
        if max_c < count:
            max_c = count
        if i == 0:
            count = 0


    print(f'#{t} {max_c}')
