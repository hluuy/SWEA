def dfs(v):
    visited[v] = True
    for i in stack[v]:
        if visited[i] == False:
            dfs(i)

T = 10
for _ in range(1, T + 1):
    t, E = map(int, input().split()) # 테스트케이스 번호 t와 길의 총 개수 E(간선)
    lst = list(map(int, input().split())) # 간선 정보를 받아 옴

    visited = [False] * 100 # 정점이 방문 되었는지?, 초기화를 시켜야하는데 정점의 최대 개수가 100개여서 하나하나 체크하기 위해서 100개 생성
    stack = [[] for _ in range(100)] # 갈 수 있는 길을 표시, 2차원 리스트에 들어가 있는 간선 정보를 인덱스 값을 통해 알 수 있도록 100개 생성

    for i in range(E):
        stack[lst[i * 2]].append(lst[i * 2 + 1]) # 간선 정보가 들어 있는 lst에서 간선 정보를 원하는 인덱스에 저장하기 위해 점화식을 만들어 append

    dfs(0)

    result = int(visited[-1])

    print(result)