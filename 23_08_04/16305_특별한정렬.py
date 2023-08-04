T = int(input())
for t in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input().split()))
    min_list = sorted(lst)
    max_list = min_list[::-1]
    result_list = []
    # while len(result_list) != len(lst):
    #     result_list.append(min_list)
    for i in range(len(lst) // 2):
        result_list.append(max_list[i])
        result_list.append(min_list[i])
        if len(result_list) == 10:
            break


    print(f'#{t}', *result_list)
