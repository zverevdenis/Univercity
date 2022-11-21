word = input()
print(word[2])
print(word[len(word) - 1])
print(word[:5])
print(word[:len(word) - 2])
for i in range(len(word)):
    if i % 2 == 0:
        print(word[i], end='')
print(' ')
for i in range(len(word)):
    if i % 2 == 1:
        print(word[i], end='')
print(' ')
word = word[::-1]
print(word)
for i in range(len(word)):
    if i % 2 == 0:
        print(word[i], end='')