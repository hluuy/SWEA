T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))
    for _ in range(M):
        lst.append(lst.pop(0))
    print(f'#{t} {lst[0]}')

# T = int(input())
# for t in range(1, T + 1):
#     N, M = map(int, input().split())
#     lst = list(map(int, input().split()))
#     front = 0
#     for i in range(M):
#         front += 1
#         if front == N:
#             front = 0
#     print(f'#{t} {lst[front]}')