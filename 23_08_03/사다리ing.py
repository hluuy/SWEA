T = int(input())
for t in range(1, T + 1):
    N = 100
    lst = [list(map(int, input().split()))for _ in range(N)]
    y = lst[99].index(2)
    x = 99
    print(lst[x][y+1]) # 0


    while y != 0 and 0 <= x < 100:
        if lst[x][y - 1] == 1:
                y = y - 1
                x -= 1
        elif lst[x][y + 1] == 1:
            y = y + 1
            x -= 1
        elif lst[x][y+1] == 0 and lst[x][y+1] == 0 :
            x -= 1
    # for _ in range(99):
    #     if lst[x][y - 1] == 1:
    #         while lst[x][y - 2] == 0:
    #             y = y - 1
    #         x -= 1
    #     elif lst[x][y + 1] == 1:
    #         while lst[x][y + 1] == 0:
    #             y = y + 1
    #         x -= 1
    #     elif lst[x][y + 1] == 0 and lst[x][y - 1] == 0:
    #         x -= 1
    # print(y)