sentence = input()
print(sentence[:sentence.find('h')] + sentence[sentence.rfind('h') + 1:])