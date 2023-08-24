# T = int(input())
# for t in range(1, T + 1):
#     N = int(input())
#     bus_info = [list(map(int, input().split()))for _ in range(N)]
#     P = int(input())
#     bus_num = [[] for _ in range(P + 1)]

#     for i in bus_info:
#         for j in range(i[0], max(i)+1):
#             bus_num[j].append(j)

#     result = []

#     for i in bus_num:
#         result.append(len(i))
#     print(f'#{t}',*result[1:])

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    bus_info = [list(map(int, input().split())) for _ in range(N)]
    P = int(input())
    bus_num = [0] * (5001)
    result = []


    for i in bus_info:
        for j in range(i[0], i[1]+1):
            bus_num[j] += 1
    for _ in range(P):
        result.append(bus_num[int(input())])

    print(f'#{t}', *result)
