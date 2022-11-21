num_list = [int(s) for s in input().split()]
for i in range(len(num_list) - 1):
    if num_list[i] < num_list[i+1]:
        print(num_list[i+1])