def dfs(v):
    visited[v] = True
    for i in stack[v]:
        if visited[i] == False:
            dfs(i)

T = int(input())
for t in range(1, T + 1):
    V, E = map(int, input().split())
    lst = [list(map(int, input().split()))for _ in range(E)]
    S, G = map(int, input().split())

    visited = [False] * (V + 1)
    stack = [[] for _ in range(V + 1)]
    for i in range(E):
        stack[lst[i][0]].append(lst[i][1])

    dfs(S)

    result = int(visited[G])

    print(f'#{t} {result}')

