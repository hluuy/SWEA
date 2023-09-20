def binary(num):
    binary = ""
    while num != 0:
        num *= 2
        if num >= 1:
            binary += "1"
            num -= 1
        else:
            binary += "0"
    return binary


T = int(input())
for t in range(1, T + 1):
    N = float(input())
    N2 = binary(N)
    if len(N2) > 12:
        print(f'#{t} overflow')
    else:
        print(f'#{t} {N2}')

