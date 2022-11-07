a = int(input())
if (a < 1000) or (a > 9999):
    print('Неверное число')
else:
    if (a // 100 % 10 == (a % 100) // 10) and (a // 1000 == a % 10):
        print('Да')
    else:
        print('Нет')