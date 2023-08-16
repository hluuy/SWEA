for t in range(1, 11):
    N = input()
    STR = input()
    result = 0
    for item in STR:
        if item.isdecimal():
            result += int(item)

<<<<<<< HEAD
    print(f'#{t} {result}')

    # for item in STR:
    #     if item.isdecimal():
    #         lst.append(int(item))
    # for i in lst:
    #     result += i
=======
    print(f'#{t} {result}')
>>>>>>> f63221fc20ba2c0d19f065bfda1944b4497c9aca
