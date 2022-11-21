d = dict()
for i in range(int(input())):
    country, *cities = input().split()
    for city in cities:
        d[city] = country
for i in range(int(input())):
    print(f"{d[input()]}")