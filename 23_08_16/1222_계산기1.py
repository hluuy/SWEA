for t in range(1, 11):
    N = input()
    STR = input()
    result = 0
    for item in STR:
        if item.isdecimal():
            result += int(item)

    print(f'#{t} {result}')

    # for item in STR:
    #     if item.isdecimal():
    #         lst.append(int(item))
    # for i in lst:
    #     result += i