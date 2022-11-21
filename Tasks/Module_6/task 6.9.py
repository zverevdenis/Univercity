word = input()
first_part = word[:len(word) // 2 + len(word) % 2]
second_part = word[len(word) // 2 + len(word) % 2:]
print(second_part + first_part)