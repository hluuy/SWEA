def inorder_traversal(T):
    if T :
        if T <= V:
            inorder_traversal(T * 2)
            result.append(arr[T-1])
            inorder_traversal(T * 2 + 1)

T = 10
for t in range(1, T + 1):
    V = int(input())
    lst = [input().split()for _ in range(V)]
    arr = []
    result = []
    for i in lst:
        for j in i:
            if j.isdecimal() == False:
                arr.append(j)

    inorder_traversal(1)
    print(f'#{t} ' + ''.join(result))
