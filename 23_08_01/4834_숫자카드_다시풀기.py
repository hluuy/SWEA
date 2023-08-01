T = int(input())
for t in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input()))
    count = [0] * 10
    for i in lst:
        count[i] += 1
    max_c = 0
    max_n = 0
    number = 10
    for item in count[10 : 0 : -1]:
        number -= 1
        if item > max_c:
            max_c = item
            max_n = number
    print(f'#{t} {max_n} {max_c}')
