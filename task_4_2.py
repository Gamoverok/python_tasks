a = [1, 2, 3, 4, 5]
summ_for = 0
for element in a:
    if element % 2 == 0:
        summ_for += 1
print('Количество четных чисел в списке по циклу For:=', summ_for)

summ_while = 0
i = 0  # timer

while i < len(a):
    if a[i] % 2 == 0:
        summ_while += 1
    i += 1
print('Количество четных чисел в списке по циклу While:=', summ_while)
