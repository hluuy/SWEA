a = int(input())

for i in range(a):
    str = input()
    num_list = [int(num) for num in str.split()]
    print(f'#{i+1} {max(num_list)}')
