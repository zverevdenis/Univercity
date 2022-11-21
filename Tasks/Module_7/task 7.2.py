d = dict()
n = int(input())
for i in range(n):
    a, b = input().split()
    d[b] = a
    d[a] = b
print(d[input()])