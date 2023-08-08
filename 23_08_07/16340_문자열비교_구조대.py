T = int(input())
for t in range(1, T + 1):
    N = input()
    M = input()
    a = 0
    NEW = []
    for i in range(len(M)-len(N)+1): # 시작위치를 i로 정함
        word = ''
        for j in range(len(N)): # word에 j개의 문자들이 들어감
            nj = j+i
            if 0 <= nj < len(M):
                word += M[i+j]
        NEW.append(word)
    for p in NEW:
        if p == N:
            a = 1

    print(f'#{t} {a}')