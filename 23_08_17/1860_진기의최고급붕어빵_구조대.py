T = int(input())
for t in range(1, T + 1):
    N, M, K = map(int,input().split()) # N = 사람 수, M = 걸리는 시간, K = 시간 M 당 만드는 개수
    cnt = 0
    cus = 0
    Q = []
    result = 1
    people = list(map(int, input().split()))
    while True:

        if cnt % M == 0 and cnt != 0:
            [Q.append(1)for _ in range(K)]
        if cnt in people:
            if len(Q) >= people.count(cnt):
                for i in range(people.count(cnt)):
                    cus += 1
                    Q.pop(0)
            else:
                result = -1
                break
        if cus == len(people):
            break
        cnt += 1
    if 0 in people:
        result = -1
    if result == 1:
        print(f'#{t} Possible')
    else:
        print(f'#{t} Impossible')

# T = int(input())
# for t in range(1, T + 1):
#     N, M, K = map(int, input().split())  # N = 사람 수, M = 걸리는 시간, K = 시간 M 당 만드는 개수
#     cnt = 0
#     cus = 0
#     Q = []
#     result = 1
#     people = list(map(int, input().split()))
#     while True:
#         cnt += 1
#         if cnt % M == 0:
#             [Q.append(1) for _ in range(K)]
#         if cnt in people:
#             if len(Q) >= 1:
#                 cus += 1
#                 Q.pop(0)
#             else:
#                 result = -1
#                 break
#         if cus == len(people):
#             break
#     if 0 in people:
#         result = -1
#     if result == 1:
#         print(f'#{t} Possible')
#     else:
#         print(f'#{t} Impossible')


        # if 0 in people:
        #     result = -1
        #     break
    # while True:
    #     cnt += 1
    #     if cnt % M == 0:
    #         bread += K
    #     for i in range(len(people)):
    #         if cnt == people[i]:
    #             cus += 1
    #             bread -= 1
    #
    #     if bread < 0:
    #         result -= 1
    #         break
    #     if cus == len(people):
    #         break
    #
    # if result == 1:
    #     print(f'#{t} Possible')
    # else:
    #     print(f'#{t} Impossible')




# for i in range(N):
    # if not cnt == 0 and cnt % people[cnt % N] == 0:
    #     cus += 1
    #     bread -= 1
    # if bread < cus:
    #     result = -1
    #     break

    #     if m == M:
    #         bread += K
    # for i in range(len(people)):
    #     for c in people:
    #         if c == people[i]:
    #             cus += 1
    # # if bread == 100:
    #     break
# print(bread)