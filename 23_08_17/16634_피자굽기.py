T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))
    Q = []
    Num = list(range(1, M+1))
    Num_list = []

    for _ in range(N):
        Q.append(lst.pop(0))
        Num_list.append(Num.pop(0))
    while len(Q) > 1:
        a = Q.pop(0) // 2
        b = Num_list.pop(0)
        if a == 0:
            if len(lst) >= 1:
                Q.append(lst.pop(0))
                Num_list.append(Num.pop(0))
        else:
            Q.append(a)
            Num_list.append(b)

    print(f'#{t} {Num_list[0]}')