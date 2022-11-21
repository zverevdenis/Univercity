num_list = [int(s) for s in input().split()]
for i in range(len(num_list)):
    if i % 2 == 1:
        print(num_list[i], num_list[i-1], end=' ')
    if i == len(num_list) - 1 and i % 2 == 0:
        print(num_list[i])