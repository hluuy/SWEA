T = int(input())
for t in range (1, T + 1):
    N = int(input())
    lst_A = [] # 1 2
    lst_B = [] # 3 5
    lst_AB = []
    for _ in range(1, N + 1):
        A, B = map(int, input().split())
        lst_A.append(A)
        lst_B.append(B)

    P = int(input())
    lst_p = []
    for i in range(1, P + 1):
        lst_p.append(i)
    result_ab1 = lst_p[lst_A[0]-1:lst_B[0]]
    result_ab2 = lst_p[lst_A[1]-1:lst_B[1]]
    # print(result_ab1)
    # print(result_ab2)
    result_AB = result_ab1 + result_ab2
    # print(result_AB)

    count = [0] * (P+1)
    for i in result_AB:
        count[i] += 1

    # print(count[1:])
    print(f'#{t}', *count[1:])
