import math
#Пользователь должен ввести x
x = float(input("Введите значение x:"))
#Вычисление f(x) в зависимости от условия
if x < 0:
#Условие f(x) = x² при x < 0    
    result = x ** 2  
else:
#Условие f(x) = √x при x ≥ 0    
    result = math.sqrt(x) 
#Вывод результата
print(f"f({x}) = {result}")
