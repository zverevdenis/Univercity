a = input()
a = a.replace('h', 'H', a.count('h') - 1)
a = a.replace('H', 'h', 1)
print(a)