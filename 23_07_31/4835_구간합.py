T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    max_v = sum(arr[:M])
    min_v = sum(arr[:M])
    value = 0

    j = 0

    for i in range(0, N-M+1):
        lst = []
        for ar in arr[i:i+M]:
            lst.append(ar)
        if sum(lst) > max_v:
            max_v = sum(lst)
        if sum(lst) < min_v:
            min_v = sum(lst)

    result = max_v - min_v
    print(f'#{tc} {result}')
