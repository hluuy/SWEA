T = int(input())
for t in range(1, T + 1):
    N = int(input())
    room = [0] * (201)
    info = [list(map(int, input().split()))for _ in range(N)]

    for i in info:
        i.sort()
        for j in range((i[0]+1)//2, (i[1]+1)//2 + 1):
            room[j] += 1
    print(f'#{t} {max(room)}')
