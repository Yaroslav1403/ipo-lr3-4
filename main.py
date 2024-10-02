import math
x = float(input("Введите значение x: "))
if x < 0:
    result = x ** 2 
else:
    result = math.sqrt(x)  
print(f"Значение функции f({x}) = {result}")
