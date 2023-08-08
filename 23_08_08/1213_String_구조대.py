T = 10
for t in range(1, T+1):
    N = int(input())
    find = input()
    full = input()
    result = 0
    for i in range(len(full)-len(find) + 1):
        j = 0
        while j < len(find):
            if full[i] != find[j]:
                break
            j += 1
            i += 1
        else:
            result += 1

    print(f'#{t} {result}')