T = int(input())
for t in range(1, T + 1):
    STR = input()
    lst = []
    for i in STR:
        lst.append(i)
        if len(lst) > 1:
            if lst[-1] == lst[-2]:
                lst.pop()
                lst.pop()

    print(f'#{t} {len(lst)}')