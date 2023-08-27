T = int(input())
for t in range(1, T + 1):
    N = int(input())
    lst = input()
    num_lst = [[] for _ in range(10)]
    max_count = 0
    max_v = 0
    for i in lst:
        num_lst[int(i)].append(int(i))
    for i in num_lst:
        if max_count < len(i):
            max_count = len(i)
            max_v = i[0]
        elif max_count >= 1:
            if max_count == len(i):
                if max_v < i[0]:
                    max_v = i[0]
    print(f'#{t} {max_v} {max_count}')
