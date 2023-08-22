def inorder(v, N): # 완전이진트리의 N은 마지막 정점
    if v <= N:
        inorder(v * 2, N) # 왼쪽 자식으로 이동
        print(lst[v], end='') # 중위순회에서 할 일
        inorder(v * 2 + 1, N) # 오른쪽 자식으로 이동

T = 10
for t in range(1, T + 1):
    N = int(input())
    lst = [0] * (N + 1) # N번 노드까지 있는 완전 이진 트리
    for _ in range(N):
        arr = list(input().split())
        lst[int(arr[0])] = arr[1]

    print(f'#{t} ', end='')
    inorder(1, N)  # root = 1
    print()