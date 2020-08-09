# Дано число найти сумму и произведение его цифр.

num = int(input('Введите число:= '))

sum_num = 0
proiz_num = 1

while num > 0:
    digit = num % 10
    sum_num += digit
    proiz_num *= digit
    num //= 10
print(f'Сумма:= {sum_num}, Произведение:= {proiz_num}')
