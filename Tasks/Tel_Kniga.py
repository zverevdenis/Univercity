d = dict()
while True:
    choice = int(input("Введите 1 для добавления или изменения телефонного контакта\n"
                       "        2 для удаления телефонного контакта\n"
                       "        3 для вывода телефонной книги\n"
                       "        4 для выхода из программы\n"))
    if choice == 1:
        number = input("Введите номер: ")
        new_number = number.replace(" ", "")
        if (len(new_number) > 12) or (len(new_number) < 10):
            print("Введен некорректный номер")
            continue
        if (number.startswith("9") is True) and (len(new_number) == 10):
            new_number = new_number.replace("9", "+79", 1)
        if number.startswith("7") is True:
            new_number = new_number.replace("7", "+7")
        if number.startswith("8") is True:
            new_number = new_number.replace("8", "+7")
        name = input("Введите имя: ")
        if name.isupper():
            name.lower()
        d[name.title()] = new_number
        print(d)
    elif choice == 2:
        name = input("Выберите имя, которое хотите удалить: ")
        name = name.title()
        del d[name]
        print(d)
    elif choice == 3:
        print(d)
    elif choice == 4:
        break