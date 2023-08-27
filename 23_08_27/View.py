T = 10
for t in range(1, T + 1):
    N = int(input())
    MAP = list(map(int, input().split()))
    count = 0
    for i in range(2, N-2):
        APT = []
        for j in range(1, 3):
            APT.append(MAP[i - j])
            APT.append(MAP[i + j])
        if MAP[i] - max(APT) > 0:
            count += MAP[i] - max(APT)

    print(f'#{t} {count}')

# T = 10
# for t in range(1, T + 1):
#     N = int(input())
#     MAP = list(map(int, input().split()))
#     count = 0
#     for i in range(2, N-2):
#         APT = []
#         APT.append(MAP[i - 2])
#         APT.append(MAP[i - 1])
#         APT.append(MAP[i + 1])
#         APT.append(MAP[i + 2])
#         if MAP[i] - max(APT) > 0:
#             count += MAP[i] - max(APT)
#
#     print(f'#{t} {count}')