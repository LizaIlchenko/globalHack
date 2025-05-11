import pandas as pd # Импортирование библиотеки пандас, для работы с табличными данными
import numpy as np # Импортирование библиотеки для работы с массивами
from scipy.interpolate import interp1d # Импортирование функции для интерполяции данных
import matplotlib.pyplot as plt # Импортирование библиотеки для вывода график
def main(points, task, out): # Создание функции с тремя аргументами
    # Загружаем данные
    p = pd.read_csv(points)
    t = pd.read_csv(task)
    # Извлекаем данные в виде массивов 
    x = p['x'].values
    y = p['y'].values
    # Используется функция interp1d для создания интерполяционной функции на основе известных точек
    func = interp1d(x, y, kind='linear', fill_value="extrapolate")
    t['y'] = func(t['x']) # Вычисление значений для у
    # Сохранение результатов
    t[['x', 'y']].to_csv(out, index=False)
    # Вывод графика и результатов
    plt.figure(figsize=(12, 6))
    # Данные для графика
    plt.scatter(x, y, color='blue', label='Исходные данные')
    # Интерполированная функция
    x_i = np.linspace(min(x), max(x), 400)
    y_i = func(x_i)
    plt.plot(x_i, y_i, color='red', label='Интерполированная функция, полученная с использованием линейной интерполяции.')
    # Добавляем подписи для графика
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('График линейной интерполяционной функции')
    plt.legend()
    # Выводим график
    plt.show()
# Вызываем функцию
main('points.csv', 'task.csv', 'results.csv')

