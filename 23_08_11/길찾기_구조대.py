for _ in range(10):
    t, E = map(int, input().split())
    road = [[] for _ in range(100)]
    arr = list(map(int, input().split()))

    for i in range(E):
        start_node = arr[i * 2]
        end_node = arr[i * 2 + 1]
        road[start_node].append(end_node)

    visited = [0] * 100
    stack = [0]

    while stack:
        now = stack.pop()

        if not visited[now]:
            visited[now] = True

            for v in road[now]:
                if not visited[v]:
                    stack.append(v)

    result = 1 if visited[99] else 0
    print(f'#{t} {result}')