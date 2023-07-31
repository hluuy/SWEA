T = 10
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    result = 0
    for i in range(N-5+1):
        lst = []

        max_v = 0
        for ar in arr[i:i+5]:
            lst.append(ar)
        for a in range(5):
            if a == 2:
                continue
            elif max_v <= lst[a]:
                max_v = lst[a]
        if lst[2] - max_v >= 1:
            result += (lst[2] - max_v)
    print(f'#{tc} {result}')
