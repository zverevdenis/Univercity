a = int(input('Введите последовательность целых неотрицательных чисел, оканчивающееся 0: \n'))
b = list()
s = 0
while a != 0:
    b.append(a)
    a = int(input())
for i in range(len(b)):
    if b[i] > b[i-1]:
        s += 1
print(s)