import math

a = int(input("Ввести знначение катета a:="))
b = int(input("вести знначение катета b:="))
c = math.sqrt(pow(a, 2) + pow(b, 2))
s = 0.5 * a * b
print("Гипотенуза прямоугольного треугольника равна:=", c)
print("Площадь прямоугольного треугольника равна:=", s)
