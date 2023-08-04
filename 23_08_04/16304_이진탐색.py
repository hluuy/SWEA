T = int(input())

def binarysearch(page, goal):
    left = 1
    right = page
    count = 0
    while left <= right:
        middle = (left + right) // 2
        count += 1
        if middle == goal:
            break
        elif middle < goal :
            left = middle
        else:
            right = middle
    return count


for t in range(1, T + 1):
    Page, A_search, B_search = map(int, input().split())

    a_binary = binarysearch(Page, A_search)
    b_binary = binarysearch(Page, B_search)


    if a_binary < b_binary:
        print(f'#{t} A')
    elif a_binary > b_binary:
        print(f'#{t} B')
    else:
        print(f'#{t} 0')

