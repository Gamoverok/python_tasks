# Найти все пары дружественных чисел, лежащих в диапазоне от 200 до 300.

for num in range(200, 301):
    sum_1 = 0
    sum_2 = 0
    for num_ost in range(1, num):
        if num % num_ost == 0:
            sum_1 += num_ost
    for j in range(1, sum_1):
        if sum_1 % j == 0:
            sum_2 += j
    if num == sum_2 and num != sum_1:
        print(sum_1, sum_2)