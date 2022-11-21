num_list = [int(s) for s in input().split()]
num_max = max(num_list)
num_min = min(num_list)
for i in range(len(num_list)):
    if num_list[i] == num_max:
        num_list[i] = num_min
    elif num_list[i] == num_min:
        num_list[i] = num_max
print(num_list)