# Дан список чисел.
# Создать новый список, каждый элемент которого равенн исходному элементу умноженному на -2.
# Вариант с for.
a = [1, 2, 3, 4, 5, 6]
b = []
for i in a:
    b.append(i * -2)
print('a = {}\nb ={}'.format(a, b))

# Вариант с while.
d = [1, 2, 3, 4, 5, 6]
c = []
i = 0
while i < len(d):
    f = d[i] * -2
    c.append(f)
    i += 1
print('d = {}\nc ={}'.format(d, c))
