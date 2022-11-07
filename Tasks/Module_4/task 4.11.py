vertical_1 = int(input('Введите первую координату по вертикали: '))
horizontal_1 = int(input('Введите первую координату по горизонтали: '))
vertical_2 = int(input('Введите вторую координату по вертикали: '))
horizontal_2 = int(input('Введите вторую координату по горизонтали: '))
if (vertical_1 % 2 == horizontal_1 % 2) == (vertical_2 % 2 == horizontal_2 % 2):
    print('Да')
else:
    print('Нет')