# def pop():
#     return lst.pop()
#
# def push(item):
#     lst.append(item)
#
#
#
# T = int(input())
# for t in range(1, T + 1):
#     sentence = input()
#     lst = []
#     for i in sentence:
#         if i == '(':
#             push(i)
#         elif i == '{':
#             push(i)
#         elif i == '[':
#             push(i)
#     for i in sentence:
#         if pop() == i :
#
# def push(item):
#     lst.append(item)
#
# def pop():
#     return lst.pop()
#
# test = input()
# lst = []
#
# for i in test:
#     if i == '(':
#         push(i)
#     elif i == ')':
#         if len(lst) == 0:
#             print("짝이 맞지 않습니다.")
#             break
#         pop()
# if len(lst) == 0:
#     print("짝이 맞습니다.")
# else:
#     print('짝이 맞지 않습니다.')
def push(item):
    lst.append(item)

def pop():
    if not lst:
        return False
    lst.pop()
    return True

test = input()
lst = []

for i in test:
    if i == '(':
        push(i)
    elif i == ')':
        if not pop():
            print("짝이 맞지 않습니다.")
            break

if not lst:
    print("짝이 맞습니다.")






