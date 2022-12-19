from pymorphy2 import MorphAnalyzer
from translate import Translator


morph = MorphAnalyzer()
translator = Translator(from_lang="ru", to_lang="en")

dialog_log = open(f"dialog.txt", mode="r", encoding='utf-8')
translate_log = open(f"translation.txt", mode="w", encoding='utf-8')

word_dict = dict()
word_count = list()
word_translation = list()

dialog_words = dialog_log.read().lower().replace("!", '').replace("?", '').replace(".", '').replace(",", '')\
    .replace("-", '').replace("\n", " ").split(" ")
for i in range(len(dialog_words)):
    dialog_words[i] = morph.parse(dialog_words[i])[0].normal_form

for i in dialog_words:
    word_dict[i] = dialog_words.count(i)

sorted_by_alphabet = dict(sorted(word_dict.items()))
sorted_by_count = sorted(sorted_by_alphabet, key=sorted_by_alphabet.get, reverse=True)

for i in word_dict:
    word_count.append(word_dict.get(i))
word_count = sorted(word_count, reverse=True)

for i in sorted_by_count:
    word_translation.append(translator.translate(i))

for i in range(len(word_count)):
    translate_log.write(f"{str(word_count[i])}|{str(word_translation[i])}|{str(sorted_by_count[i])}\n")

dialog_log.close()
translate_log.close()