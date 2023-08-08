T = int(input())
for t in range(1, T + 1):
    word = input()
    result = 0
    for i in range(len(word)//2+1):
        if word[i] == word[-i-1]:
            result = 1
        else:
            result = 0
            break
    print(f'#{t} {result}')