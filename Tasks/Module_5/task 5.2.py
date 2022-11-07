a = int(input("Введите число: "))
n = 0
while 2 ** (n + 1) <= a:
    n += 1
print(f"{n}, {2 ** n}")