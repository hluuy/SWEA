T = int(input())
for t in range(1, T + 1):
    STR = input()
    lst = []

    for i in STR:
        if i in '(){}[]':
            lst.append(i)
            if len(lst) > 1:
                if (lst[-1] == ')' and lst[-2] == '(') or (lst[-1] == '}' and lst[-2] == '{') or (
                        lst[-1] == ']' and lst[-2] == '['):
                # if lst[-1] + lst[-2] == '(,)' or '{,}' or '[,]': 이거 왜 안됨
                    lst.pop()
                    lst.pop()
    result = 0
    if len(lst) >= 1:
        result = 0
    else:
        result = 1

    print(f'#{t} {result}')

    # result = 0
    # if len(lst) > 0:
    #     pass
    # else:
    #     result = 1

    # result = ''
    # for i in lst:
    #     result += i
    # if len(result) > 0:
    #     result = 0
    # else:
    #     result = 1
    #
