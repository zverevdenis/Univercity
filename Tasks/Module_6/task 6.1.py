num_list = [int(s) for s in input().split()]
for i in range(len(num_list)):
    if num_list[i] % 2 == 1:
        print(num_list[i])