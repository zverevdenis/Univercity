vertical = int(input('Введите координату по вертикали: '))
horizontal = int(input('Введите координату по горизонтали: '))
if vertical % 2 == horizontal % 2:
    print('Чёрная')
else:
    print('Белая')