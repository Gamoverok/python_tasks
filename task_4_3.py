# Дан словарь. Присвоить ключу число равное длинне ключа.Вывести список полученных ключей
# Реализация цикла For.
s_lov = {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
for key in list(s_lov.keys()):
    s_lov[f'{key}{len(key)}'] = s_lov.pop(key)
print('Через цикл For:', s_lov)

# Реализация цикла While.
s_lov = {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
i = 0  # счётчик
keys = list(s_lov.keys())  # список ключей
while i < len(keys):
    s_lov[f'{keys[i]}{len(keys[i])}'] = s_lov.pop(keys[i])
    i += 1
print('Через цикл While:', s_lov)
