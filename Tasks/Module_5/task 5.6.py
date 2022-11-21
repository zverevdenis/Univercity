a = int(input('Введите число: '))
b = b1 = 1
i = 2
while a >= b1:
    if a == b1:
        print(i)
        break
    b_sum = b + b1
    b = b1
    b1 = b_sum
    i += 1
if b1 > a:
    print('-1')