T = int(input())
for t in range(1, T + 1):
    N = int(input())
    price = list(map(int, input().split()))
    buy = 0
    sell = 0
    low_p = 10000
    high_p = 0
    count = 0
    for i in range(N):
        if low_p > price[i]:
            low_p = price[i]
        if high_p < price[i]:
            high_p = price[i]
    for i in range(N):
        if low_p < price[i]:
            pass
        elif low_p == price[i]:
            buy += high_p - price[i]
        elif high_p == price[i]:
            sell += buy
            buy = 0
        elif price[i] < (low_p + high_p) // 2:
            if price[i] > low_p:
                sell += buy
                buy = 0
        elif price[i] > (low_p + high_p) // 2:
            sell += buy
            buy = 0
    print(sell)









    # print(f'#{t} {}')