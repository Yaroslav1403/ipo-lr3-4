import math
#Пользователь должен ввести x
x = float(input("Введите значение x:"))
#Вычисление f(x) в зависимости от условия
if x < 0:
    result = x ** 2  #условие f(x) = x² при x < 0
else:
    result = math.sqrt(x)  #условие f(x) = √x при x ≥ 0
#Вывод результата
print(f"f({x}) = {result}")
