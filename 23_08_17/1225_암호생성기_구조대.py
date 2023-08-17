T = 10
for t in range(1, T + 1):
    tc = int(input())
    lst = list(map(int, input().split()))

    i = 1  # while문 연습하기
    while True:
        v = lst.pop(0) - i
        if v <= 0:
            lst.append(0)
            break
        lst.append(v)
        i = (i % 5) + 1
    result = ''
    for i in lst:
        result += str(i)
        result += ' '

    print(f'#{t} {result}')