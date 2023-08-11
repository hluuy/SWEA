for _ in range(1, 11):
    t, E = map(int, input().split()) # 테스트 케이스 번호와 간선 수를 받음
    road = [[]for _ in range(100)] # 해당 노드에서 다른 노드로의 간선 정보를 담을 빈 리스트 생성
    arr = list(map(int, input().split())) # 간선 정보를 입력

    for i in range(E):
        start_node = arr[i * 2] # 입력 받은 arr에서 출발 노드를 가져옴
        end_node = arr[i * 2 + 1] # 입력 받은 arr에서 도착 노드를 가져옴
        road[start_node].append(end_node) # 각 노드에서 출발했을 때, 도착하는 노드들을 출발 노드 칸에 넣음
        # 0에서 출발 했을 때, 도착 노드는 1, 2라서 road[0]에는 [1, 2]가 들어있고
        # 1에서 출발 했을 때, 도착 노드는 4, 3이라서 road[1]에는 [4, 3]이 들어있다.


    visited = [0] * 100 # 한 번 왔던 길인지 확인을 위해 False인 리스트를 만들어주고
    stack = [0] # 스택에 제일 처음 출발하게 될 0을 넣는다

    while stack: # stack이 비어있을 때까지 반복
        now = stack.pop() # now값은 stack의 최상단(현재 위치)
        if not visited[now]: # vistied[now]가 True가 아니라면(한 번도 들린 적이 없다면)
            visited[now] = True # visited[now]의 값을 True로

            for v in road[now]: # 현재 위치에서 도착할 수 있는 노드를 순회하며
                if not visited[v]: # visited[v]가 True가 아니라면(한 번도 들린 적이 없다면)
                    stack.append(v) # stack에 v값을 추가

    result = 0
    if visited[99]: # 목표지점인 99가 True라면(99에 도달하여 False에서 True로 값이 변환되어 있다면)
        result = 1 # result에 1을 반환
    else: # 그게 아닌 경우
        pass # 패스
    print(f'#{t} {result}')