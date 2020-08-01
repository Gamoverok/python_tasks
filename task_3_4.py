word = (input("Ввести строку:"))
word_sr = int(len('word') / 2)  # Получаем средний индекс введенной строки.
word_centr = word[word_sr]  # Преобразуем в список.
print(word_centr)
if word_centr == word[0]:
    print(word[1:-1])  # Строка между первым и последним символом,введенной строки.
