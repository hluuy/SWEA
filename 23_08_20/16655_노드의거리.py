def bfs(S, G):
    visited = [0] * (V + 1)
    visited[S] = 1
    Q = []
    Q.append(S)
    while Q:
        r = Q.pop(0)
        if r == G:
            return visited[r] -1
        for i in stack[r]:
            if visited[i] == 0:
                visited[i] = visited[r] + 1
                Q.append(i)
    return 0

T = int(input())
for t in range(1, T + 1):
    V, E = map(int, input().split())
    stack = [[] for _ in range(V + 1)]
    for i in range(E):
        a, b = map(int, input().split())
        stack[a].append(b)
        stack[b].append(a)
    S, G = map(int, input().split())

    ans = bfs(S, G)

    print(f'#{t} {ans}')

# def bfs(S, G):
#     visited = [0] * (V + 1)
#     visited[S] = 1
#     Q = []
#     Q.append(S)
#     while Q:
#         r = Q.pop(0)
#         if r == G:
#             return visited[r] -1
#         for i in stack[r]:
#             if visited[i] == 0:
#                 visited[i] = visited[r] + 1
#                 Q.append(i)
#     return 0
#
# T = int(input())
# for t in range(1, T + 1):
#     V, E = map(int, input().split())
#     # visited = [0] * (51)
#     stack = [[] for _ in range(V + 1)]
#     # Q = []
#     for i in range(E):
#         a, b = map(int, input().split())
#         stack[a].append(b)
#         stack[b].append(a) # 양방향 그래프로 바꿔주기
#     # lst = [list(map(int, input().split()))for _ in range(E)]
#     S, G = map(int, input().split())
#
#     ans = bfs(S, G)
#
#     print(f'#{t} {ans}')