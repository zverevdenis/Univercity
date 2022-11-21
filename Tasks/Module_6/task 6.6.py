num_list = [int(s) for s in input().split()]
num_list_1 = [int(s) for s in input().split()]
for i in range(len(num_list)):
    for j in range(len(num_list_1)):
        if num_list[i] == num_list_1[j]:
            print(num_list[i], end=' ')