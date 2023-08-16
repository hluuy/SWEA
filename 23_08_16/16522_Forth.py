T = int(input())
for t in range(1, T + 1):
    STR = list(map(str, input().split()))
    stack = []
    for item in STR:
        if item.isdecimal():
            stack.append(int(item))
        if item == '+':
            if len(stack) >= 2:
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(num1 + num2)
            else:
                print(f'#{t} error')
                break
        elif item == '*':
            if len(stack) >= 2:
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(num1 * num2)
            else:
                print(f'#{t} error')
                break
        elif item == '-':
            if len(stack) >= 2:
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(num1 - num2)
            else:
                print(f'#{t} error')
                break
        elif item == '/':
            if len(stack) >= 2:
                num2 = stack.pop()
                num1 = stack.pop()
                if num2 == 0:
                    print(f'#{t} error')
                    break
                stack.append(num1 // num2)
            else:
                print(f'#{t} error')
                break
        if item == '.':
            if len(stack) == 1:
                print(f'#{t} {stack[0]}')
            else:
                print(f'#{t} error')
