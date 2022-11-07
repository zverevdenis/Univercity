a = int(input())
if (a < 100) or (a > 999):
    print('Неверное число')
else:
    if ((a % 100) // 10 > int(a / 100)) & ((a % 100) // 10 < a % 10):
        print('Да')
    else:
        print('Нет')