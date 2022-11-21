d = dict()
sorted_d = dict()
n = int(input())
for i in range(n):
    for word in input().split():
        d[word] = d.get(word, 0) + 1
sorted_keys = reversed(sorted(d, key=d.get))
for i in sorted_keys:
    sorted_d[i] = d[i]
print(sorted_d.items())