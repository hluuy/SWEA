a= int(input())

num_list = [int(num) for num in input().split()]
num_list.sort()

middle = num_list[a // 2]
print(middle)
