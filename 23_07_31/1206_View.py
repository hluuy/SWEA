# T = 10
# for tc in range(1, T+1):
#     N = int(input())
#     arr = list(map(int, input().split()))
#     result = 0
#     for i in range(N-5+1):
#         lst = []

#         max_v = 0
#         for ar in arr[i:i+5]:
#             lst.append(ar)
#         for a in range(5):
#             if a == 2:
#                 continue
#             elif max_v <= lst[a]:
#                 max_v = lst[a]
#         if lst[2] - max_v >= 1:
#             result += (lst[2] - max_v)
#     print(f'#{tc} {result}')


T = 10
for t in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    cnt = 0

    for i in range(2, N-2):
        view = []
        if lst[i] - lst[i-1] > 0 and lst[i] - lst[i-2] > 0 and lst[i] - lst[i+1] > 0 and lst[i] - lst[i+2] > 0:
            view.append(lst[i] - lst[i - 1])
            view.append(lst[i] - lst[i - 2])
            view.append(lst[i] - lst[i + 1])
            view.append(lst[i] - lst[i + 2])
            if view:
                cnt += min(view)
        print(f'#{t} {cnt}')