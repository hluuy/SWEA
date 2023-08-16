T = int(input())
for t in range(1, T + 1):
    N = int(input())
    lst = [list(map(int, input().split()))for _ in range(N)]
    visited = [0] * 201
    for i in lst:
        a, b = min(i[0],i[1]), max(i[0],i[1])
        a = (a + 1) // 2
        b = (b + 1) // 2
        for j in range(a, b + 1):
            visited[j] += 1

    print(f'#{t} {max(visited)}')

# T = int(input())
# for t in range(1, T + 1):
#     N = int(input())
#     lst = [list(map(int, input().split()))for _ in range(N)]
#     cnt = 0
#     visited = [0] * 401
#     for i in lst:
#         a, b = min(i[0],i[1]), max(i[0],i[1])
#         if a % 2 == 0:
#             pass
#         else:
#             a = a + 1
#         if b % 2 == 0:
#             pass
#         else:
#             b = b + 1
#         for j in range(a, b + 1):
#             visited[j] += 1
#
#     print(f'#{t} {max(visited)}')

# T = int(input())
# for t in range(T):
#     N = int(input())
#     lst = [list(map(int, input().split())) for _ in range(N)]
#     cnt = 0
#     v = [0] * 401
#     for l in lst:
#         a, b = min(l[0], l[1]), max(l[0], l[1])
#         a = a - 1 if a % 2 == 0 else a
#         b = b + 1 if b % 2 == 1 else b
#         for i in range(a, b + 1):
#             v[i] += 1
#
#     print(f'#{t + 1}', max(v))