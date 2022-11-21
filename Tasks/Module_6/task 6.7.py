num_list = [int(s) for s in input().split()]
num_set = set()
for i in range(len(num_list)):
    print('НЕТ' if num_list[i] not in num_set else 'ДА', end=' ')
    num_set.add(num_list[i])