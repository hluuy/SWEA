T = int(input())
for t in range(1, T + 1):
    original = input()
    original_lst = []
    n = len(original)
    reset = [0] * n
    count = 0
    for item in original:
        original_lst.append(item)
    for i in range(len(original_lst)):
        if original_lst[i] == '0':
            if reset[i] != 0:
                reset[i:] = [0] * len(reset[i:])
                count += 1
        elif original_lst[i] == '1':
            if reset[i] != 1:
                reset[i:] = [1] * len(reset[i:])
                count += 1
    print(f'#{t} {count}')
