T = int(input()) # T로 테스트케이스 받기
for t in range(1, T + 1): # 테스트케이스만큼 돌리기
    N, M = map(int, input().split()) # N, M으로 맵 크기 가져오기
    lst = [list(map(int, input().split()))for _ in range(N)] # 크기를 바탕으로 맵 가져오기
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0] # 델타탐색을 위한 범위 설정
    max_v = 0 # 최대 값을 구하기 위해 맥스 값 초기화
    for i in range(N): # N만큼 돌고
        for j in range(M): # M만큼 도는데
            a = lst[i][j] # 임의의 점 정해서
            s = 0
            for p in range(4): # 주변 델타 탐색 돌리면서
                for q in range(1, a+1): # 임의의 점의 수만큼 범위가 늘어나고
                    ni, nj = i + di[p] * q, j + dj[p] * q # 늘어난 범위의 좌표
                    if 0 <= ni < N and 0 <= nj < M: # 늘어난 범위가 맵을 안벗어났으면
                        s += lst[ni][nj] # s에 해당 범위의 값 저장
            if max_v < a+s: # 만약 임의의 점과 범위를 돌려 더한 값들이 max_v보다 작으면
                max_v = a+s # max_v에 a+s 값 할당

    print(f'#{t} {max_v}') # 출력
