d = dict()
for i in range(int(input())):
    name, *operations = input().split()
    d[name] = operations
access = {'read': 'R', 'write': 'W', 'execute': 'X'}
for i in range(int(input())):
    acc, nam = input().split()
    print('OK' if access[acc] in d[nam] else 'Access denied')