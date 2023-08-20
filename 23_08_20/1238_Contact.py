def bfs(s):
    visited = [0] * 101
    Q = []
    visited[s] = 1
    Q.append(s)
    max_lst = []
    while Q:
        d = Q.pop(0)
        for i in stack[d]:
            if visited[i] == 0:
                visited[i] = visited[d] + 1
                Q.append(i)
    max_v = max(visited)
    for i in range(len(visited)):
        if visited[i] == max_v:
            max_lst.append(i)

    return max(max_lst)

T = 10
for t in range(1, T + 1):
    l, start = map(int, input().split())
    MAP = list(map(int, input().split()))
    stack = [[] for _ in range(101)]
    for i in range(l // 2):
        stack[MAP[i * 2]].append(MAP[i * 2 + 1])
    ans = bfs(start)

    print(f'#{t} {ans}')
