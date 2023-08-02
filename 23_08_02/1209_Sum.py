
for t in range(1, 11):
    T = int(input())
    Numbers = [list(map(int, input().split()))for _ in range(100)]
    row = len(Numbers)
    col = len(Numbers[0])
    max_row = 0
    max_col = 0
    max_line = 0
    max_reverse_line = 0
    max_v = 0
    sum_row = 0
    sum_col = 0
    sum_line = 0
    sum_reverse_line = 0
    for i in range(row):
        lst = []
        for j in range(col):
            lst.append(Numbers[i][j])
            sum_row = sum(lst)
            for _ in range(100):
                if sum_row > max_row:
                    max_row = sum_row


    for j in range(col):
        lst = []
        for i in range(row):
            lst.append(Numbers[i][j])
            sum_col = sum(lst)
            for _ in range(100):
                if sum_col > max_col:
                    max_col = sum_col


    for i in range(row):
        lst = []
        lst.append(Numbers[i][i])
        sum_line += sum(lst)
        if sum_line > max_line:
            max_line = sum_line


    for i in range(row):
        lst = []
        lst.append(Numbers[99-i][i])
        sum_reverse_line += sum(lst)
        if sum_reverse_line > max_reverse_line:
            max_reverse_line = sum_reverse_line


    if max_v < max_row:
        max_v = max_row
    if max_v < max_col:
        max_v = max_col
    if max_v < max_line:
        max_v = max_line
    if max_v < max_reverse_line:
        max_v = max_reverse_line

    print(f'#{t} {max_v}')





    # line = list(Numbers[i][i] for i in range(100))
    # sum_line = sum(line)
    # print(sum_line)
    # reverse_line = [Numbers[i][99-i]for i in range(100)]
    # sum_reverse_line = sum(line)
    # print(sum_reverse_line)

            # sum_row = sum(Numbers[i][j])
            # print(Numbers[i][j], end=' ')
    #         if sum(Numbers[i][j]) > max_row:
    #             max_row = sum(Numbers[i][j])
    # print(max_row)


