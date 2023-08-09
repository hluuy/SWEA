# T = int(input())
# for t in range(1, T + 1):
#     N = int(input())
#     price = list(map(int, input().split()))
#     buy = 0
#     sell = 0
#     low_p = 10000
#     high_p = 0
#     avg_p = (low_p + high_p) // 2
#     count = 0
#     for i in range(N):
#         if low_p > price[i]:
#             low_p = price[i]
#         if high_p < price[i]:
#             high_p = price[i]
#     for i in range(N):
#         if price[i] == high_p:
#             sell += buy
#             buy = 0
#             change_high = price.pop(high_p)
#             if high_p < price[i]:
#                 high_p = price[i]
#         elif price[i] <= low_p:
#             buy += high_p - price[i]
#         elif price[i] < avg_p:
#             if high_p - price[i] < low_p:
#                 pass
#             elif high_p - price[i] >= low_p:
#                 buy += high_p - price[i]
#         elif price[i] >= avg_p:
#             sell += buy
#             buy = 0
#
#
#
#     print(buy)
# T = int(input())
# for t in range(1, T + 1):
#     N = int(input())
#     price = list(map(int, input().split()))
#     buy = 0
#     sell = 0
#     low_p = 10000
#     high_p = 0
#     avg_p = (low_p + high_p) // 2
#     count = 0
#     for i in range(N):
#         if low_p > price[i]:
#             low_p = price[i]
#         if high_p < price[i]:
#             high_p = price[i]
#     for i in range(N):
#         if price[i] == high_p:
#             sell += buy
#             buy = 0
#             remaining_prices = price[i + 1:]
#             if remaining_prices:
#                 high_p = max(remaining_prices)
#             else:
#                 high_p = 0
#         elif price[i] <= low_p:
#             buy += high_p - price[i]
#         elif price[i] < avg_p:
#             if high_p - price[i] < low_p:
#                 pass
#             elif high_p - price[i] >= low_p:
#                 buy += high_p - price[i]
#         elif price[i] >= avg_p:
#             sell += buy
#             buy = 0
#
#     print(f'#{t} {sell}')
T = int(input())
for t in range(1, T + 1):
    N = int(input())
    price = list(map(int, input().split()))
    buy = 0
    sell = 0
    low_p = 10000
    high_p = 0

    for p in price:
        if low_p > p:
            low_p = p
        if high_p < p:
            high_p = p

    for p in price:
        if p == high_p:
            sell += buy
            buy = 0
            high_p = max(price[price.index(p) + 1:]) if p in price[price.index(p) + 1:] else 0
        elif p <= low_p:
            buy += high_p - p
        elif p < (low_p + high_p) // 2 and high_p - p >= low_p:
            buy += high_p - p
        else:
            sell += buy
            buy = 0

    print(f'#{t} {sell}')
