T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    max_v = 0
    min_v = 0
    for i in range(1, N):
        if arr[min_v] > arr[i]:
            min_v = i
        if arr[max_v] <= arr[i]:
            max_v = i
    result = 0
    if max_v > min_v:
        result = max_v - min_v
    elif max_v < min_v:
        result = (max_v - min_v) * (-1)

    print(f'#{t} {result}')
