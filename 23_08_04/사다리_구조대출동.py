T = 10

for _ in range(T):
    TC = int(input())
    N = 100
    lst = [list(map(int, input().split()))for _ in range(N)]
    x = lst[99].index(2)
    y = 99
    # print(lst[y][x]) # 2


    while y != 0:

        if x >= 1 and lst[y][x - 1] == 1:
            while x >= 1 and lst[y][x - 1] != 0 :
                x = x - 1

        elif x < 99 and lst[y][x + 1] == 1:
            while x < 99 and lst[y][x + 1] != 0:
                x = x + 1

        y -= 1
    print(f'#{TC} {x}')