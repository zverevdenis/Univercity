d = dict()
n = int(input())
for i in range(n):
    a = input().split()
    for j in a:
        d[j] = d.get(j, 0) + 1
m = max(d.values())
b = set()
for key in d:
    if d[key] == m:
        b.add(key)
print(sorted(b)[0])