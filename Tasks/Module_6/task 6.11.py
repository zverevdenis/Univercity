sentence = input()
a = sentence[sentence.find('h'):sentence.rfind('h')]
print(sentence[:sentence.find('h')] + a[::-1] + sentence[sentence.rfind('h') + 1:])