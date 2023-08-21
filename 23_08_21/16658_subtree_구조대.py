def preorder(n):
    count = 1
    if not ch1[n] == 0:
        count += preorder(ch1[n])
    if not ch2[n] == 0:
        count += preorder(ch2[n])
    return count


T = int(input())
for t in range(1, T + 1):
    E, N = map(int, input().split())
    lst = list(map(int, input().split()))
    ch1 = [0] * (E + 2)
    ch2 = [0] * (E + 2)
    for i in range(E):
        p, c = lst[i * 2], lst[i * 2 + 1]
        if ch1[p] == 0:
            ch1[p] = c
        else:
            ch2[p] = c
    a = preorder(N)
    print(a)
