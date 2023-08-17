T = int(input())
for t in range(1, T + 1):
    N, M, K = map(int,input().split()) # N = 사람 수, M = 걸리는 시간, K = 시간 M 당 만드는 개수
    cnt = 0
    bread = 0
    cus = 0
    result = 0
    people = list(map(int, input().split()))
    while True:
        cnt += 1
        if cnt % M == 0:
            bread += K
        # for i in range(N):
        if not cnt == 0 and cnt // people[cnt % N] == 1:
            cus += 1
            bread -= 1
        if bread < cus:
            result = -1
            break

        #     if m == M:
        #         bread += K
        # for i in range(len(people)):
        #     for c in people:
        #         if c == people[i]:
        #             cus += 1
        # # if bread == 100:
        #     break
        # print(bread)
    print(result)


    print(f'#{t} Possible')