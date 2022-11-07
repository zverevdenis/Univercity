a = float(input("Введите начальную дистанцию: "))
b = float(input("Введите конечную дистанцию: "))
s = 1
while a < b:
    a *= 1.1
    s += 1
print(s)