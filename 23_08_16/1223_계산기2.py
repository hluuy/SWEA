T = 10
for t in range(1, T + 1):
    N = int(input())
    STR = list(map(str, input().split('+')))
    STR_2nd = []
    STR_3rd = []
    STR_4th = []
    STR_5th = []
    result = 0
    for item in STR:
        if item.isdecimal():
            STR_2nd.append(int(item))
        else:
            STR_3rd.append(item)
    for item in STR_2nd:
        result += item
    for item in STR_3rd:
        STR_4th.append(item)
    for item in STR_4th:
        items = list(map(int, item.split('*')))
        mul = 1
        for i in items:
            mul *= i
        STR_5th.append((mul))
    for item in STR_5th:
        result += item
    print(f'#{t} {result}')
