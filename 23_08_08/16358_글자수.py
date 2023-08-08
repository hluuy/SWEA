T = int(input())
for t in range(1, T + 1):
    in_list = list(input())
    out_list = list(input())
    result = 0
    for i in in_list:
        a = 0
        for j in out_list:
            if j == i:
                a += 1
        if result < a:
            result = a
    print(f'#{t} {result}')
