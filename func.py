import pandas as pd
import numpy as np
from numpy.polynomial import Polynomial
# Загружаем данные
df = pd.read_csv('points.csv')
# Извлекаем данные в виде массивов 
x = df['x'].values
y = df['y'].values
# Выполняем апроксимацию полиномом третьей степени
coef = Polynomial.fit(x, y, 3).convert().coef
# Создали полиномиальную функцию
func = np.poly1d(coef)
# Форматирование функции
def format(c):
    t = []
    for p, f in enumerate(c):
        if f != 0:
            ter = f"{f:.2e} * x^{p}" if p != 0 else f"{f:.2e}"
            t.append(ter)
    return "f(x) = " + " + ".join(reversed(t))
# Вывод выражения функции
print("Аналитическое выражение функции:")
print(format(coef))
# Использования функции для вычисления y
x_v = -9999.5  # Задаем значение x
y_v = func(x_v)
print(f"Для x = {x_v}, y = {y_v}")

