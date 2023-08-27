T = int(input())
for t in range(1, T + 1):
    N, K = map(int, input().split())
    done = list(map(int, input().split()))
    students = [[] for _ in range(N+1)]
    didnt = []
    for i in done:
        students[i].append(i)
    for i in range(len(students)):
        if len(students[i]) < 1:
            didnt.append(i)
    print(f'#{t}', *didnt[1:])