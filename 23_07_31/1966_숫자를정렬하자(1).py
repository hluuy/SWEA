T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    lst = []
    for item in arr:
        lst.append(item)
        lst.sort()

    print(f'#{tc}', *lst)

