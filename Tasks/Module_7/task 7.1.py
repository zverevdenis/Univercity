dct = {}
for key in input().split():
    dct[key] = dct.get(key, 0) + 1
    print(dct[key] - 1)