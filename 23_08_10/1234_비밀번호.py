T = 10
for t in range(1, T + 1):
    cnt, NUM = map(str, input().split())
    lst = []

    for i in NUM:
        lst.append(i)
        if len(lst) > 1:
            if lst[-1] == lst[-2]:
                lst.pop()
                lst.pop()
    result = ''
    for i in lst:
        result += i

    print(f'#{t} {result}')
