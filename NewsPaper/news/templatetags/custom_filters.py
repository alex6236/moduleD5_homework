from django import template
import re
# import os

# current_directory = os.getcwd()
# contents = os.listdir(current_directory)
# print(contents)

register = template.Library()

@register.filter(name='censor')
def censor(value):
    # Открываем файл "words.txt" в режиме чтения 
    with open('words.txt', 'r', encoding='utf-8') as f:
        # читаем файл, разделяем на отдельные слова, сохраняя их в переменную "bad_words"
        bad_words = f.read().split()
        for w in bad_words:
            # применяем регулярное выражение r'\b{}\b'.format(w) это чтобы слово заменялось целиком, а то у мня сначала было что только часть слова фильтровалась корень-то у матерных слов похожий :)
            word = r'\b{}\b'.format(w)
            # при совпадении меняем слово на '!п-'+'и-'*len(w)+'п!' получается п-и-и-и-и-п, длина зависит от длины слова которое меняем
            value = re.sub(word, '!п-'+'и-'*len(w)+'п!', value)
        return value