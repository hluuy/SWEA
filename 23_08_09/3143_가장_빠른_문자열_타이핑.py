T = int(input())
for t in range(1, T + 1):
    A, B = input().split()
    C = A.count(B)
    result = len(A)-(len(B)*C)+C
    print(f'#{t} {result}')