import pandas as pd
import numpy as np
from numpy.polynomial import Polynomial
import matplotlib.pyplot as plt
def main(points, task, out):
    p = pd.read_csv(points)
    t = pd.read_csv(task)
    # Извлечение данных
    x = p['x'].values
    y = p['y'].values
    # Аппроксимация полиномом третьей степени
    c = Polynomial.fit(x, y, 3).convert().coef
    func = np.poly1d(c)
    # Вычисление значений y для x из task
    t['y_p'] = func(t['x'])
    # Сохранение результатов
    t[['x', 'y_p']].to_csv(out, index=False)
    plt.figure(figsize=(12, 6))
    plt.scatter(x, y, color='blue', label='Исходные данные')
    x_poly = np.linspace(min(x), max(x), 400)
    y_poly = func(x_poly)
    plt.plot(x_poly, y_poly, color='green', linestyle='--', label='Полиномиальная аппроксимация, полученная с использованием полинома третьей степени')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('График полиномиальной аппроксимации функции')
    plt.legend()
    plt.show()
main('points.csv', 'task.csv', 'p_results.csv')
