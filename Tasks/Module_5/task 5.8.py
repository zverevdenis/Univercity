a = int(input('Введите последовательность чисел:\n'))
b = list()
b.append(a)
s = max = i = 1
while a != 0:
    a = int(input())
    b.append(a)
    if b[i] == b[i-1] and i != 1:
        s += 1
    else:
        s = 1
    if s > max:
        max = s
    i += 1
print(max)