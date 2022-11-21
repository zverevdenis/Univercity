d = dict()
n = int(input())
for i in range(n):
    a, b = input().split()
    d.setdefault(a, 0)
    d[a] = int(d[a]) + int(b)
print(sorted(d.items()))