T = int(input())
for t in range(1, T + 1):
    N = input()
    lst = list(map(str, input().split()))
    zero = one = two = three = four = five = six = seven = eight = nine = 0
    for i in range(len(lst)):
        if lst[i] == "ZRO":
            zero += 1
        elif lst[i] == "ONE":
            one += 1
        elif lst[i] == "TWO":
            two += 1
        elif lst[i] == "THR":
            three += 1
        elif lst[i] == "FOR":
            four += 1
        elif lst[i] == "FIV":
            five += 1
        elif lst[i] == "SIX":
            six += 1
        elif lst[i] == "SVN":
            seven += 1
        elif lst[i] == "EGT":
            eight += 1
        elif lst[i] == "NIN":
            nine += 1
    print(f'#{t}\n{"ZRO " * zero}{"ONE " * one}{"TWO " * two}{"THR " * three}{"FOR " * four}{"FIV " * five}{"SIX " * six}{"SVN " * seven}{"EGT " * eight}{"NIN " * nine}')

# T = int(input())
# number_names = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
#
# for t in range(1, T + 1):
#     N = input()
#     lst = list(input().split())
#     count = {name: 0 for name in number_names}
#
#     for num in lst:
#         count[num] += 1
#
#     result = ' '.join([f'{name} ' * count[name] for name in number_names])
#     print(f'#{t}\n{result}')
