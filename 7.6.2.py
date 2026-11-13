import re

def longest_word(text):
    # Находим все слова (буквы и цифры)
    words = re.findall(r"\w+", text)
    # Возвращаем самое длинное слово или None, если текст пустой
    return max(words, key=len) if words else None

print(longest_word("Программирование — это интересно, правда?"), "|", longest_word("... !!!"))