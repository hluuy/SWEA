def dfs(v):
    visited[v] = True
    for i in stack[v]:
        if visited[i] == False:
            dfs(i)

T = 10
for _ in range(T):
    t, E = map(int, input().split())
    arr = list(map(int, input().split()))

    visited = [False] * 100
    stack = [[] for _ in range(100)]

    for i in range(E):
        stack[arr[i*2]].append(arr[i * 2 + 1])

    dfs(0)
    result = int(visited[-1])

    print(result)