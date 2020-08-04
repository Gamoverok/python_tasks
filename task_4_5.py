# Составить список чисел Фибоначчи содержащий 15 элементов.

n = int(input("Введите числа для формирования списка:="))
fib1 = fib2 = 1
if n < 2:
    quit()
print(fib1, end=' ')
print(fib2, end=' ')
for i in range(2, n):
    fib1, fib2 = fib2, fib1 + fib2
    print(fib2, end=' ')

print()
