# def dfs(v):
#     visited[v] = True
#     for i in stack[v]:
#         if visited[i] == False:
#             dfs(i)
#
# T = int(input())
# for t in range(1, T + 1):
#     V, E = map(int, input().split())
#     lst = [list(map(int, input().split()))for _ in range(E)]
#     S, G = map(int, input().split())
#
#     visited = [False] * G
#     stack = [[]for _ in range(G)]
#
#     for i in range(E):
#         stack[lst[i * 2]].append(lst[i * 2 + 1])
#
#     dfs(S)
#
#     result = int(visited[-1])
#
#     print(result)
#
#     # print(f'#{t}')
def dfs(v):
    visited[v] = True
    for i in stack[v]:
        if visited[i] == False:
            dfs(i)

T = int(input())
for t in range(1, T + 1):
    V, E = map(int, input().split())
    stack = [[] for _ in range(V + 1)]
    for i in range(E):
        a, b = map(int, input().split())
        stack[a].append(b)
    # lst = [list(map(int, input().split()))for _ in range(E)]
    S, G = map(int, input().split())

    visited = [False] * (V + 1)

    dfs(S)

    result = int(visited[G])

    print(f'#{t} {result}')

