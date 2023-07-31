a = int(input())

for i in range(a):
    str = input()
    num_list = list(map(int, str.split()))
    hole = [number for number in num_list if number % 2 == 1]
    total = sum(hole)
    print(f'#{i+1} {total}')
