T = int(input())
for t in range(1, T + 1):
    pipe = list(input())
    cnt = 0
    ans = 0
    for i in range(len(pipe)):
        if pipe[i] == '(':
            cnt += 1
        elif pipe[i] == ')':
            if pipe[i-1] != '(':
                cnt -= 1
                ans += 1
            else:
                cnt -= 1
                ans += cnt
    print(f'#{t} {ans}')
