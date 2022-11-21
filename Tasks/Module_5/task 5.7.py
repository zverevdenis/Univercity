a = int(input('Введите номер числа Фибоначчи: ')) - 2
b = b1 = 1
while a != 0:
    b_sum = b + b1
    b = b1
    b1 = b_sum
    a -= 1
print(b1)