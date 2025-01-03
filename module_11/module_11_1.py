import numpy as np
import random
import matplotlib.pyplot as plt

# Создание массива и базовые операции
# Создай массив из чисел от 5 до 16 невключительно.
arr = np.arange(5, 16)

# Выведи созданный массив в консоль.
print(arr)

# Умножь все элементы массива на 3 и добавь 10. Выведи результат.
arr = arr * 3 + 10
print(arr, '\n')

# Создай массив из 15 случайных чисел от 1 до 50.
arr = []
for i in range(15):
  num = random.randint(1, 51)
  arr.append(num)

arr = np.array(arr)

# Найди и выведи:
#   Сумму всех элементов.
print(f'Сумма всех элементов массива: {np.sum(arr)}')

#   Среднее значение.
print(f'Среднее значение всех элементов массива: {np.mean(arr)}')

#   Минимальное и максимальное значения.
print(f'Минимальное значение элементов массива: {np.min(arr)}')
print(f'Максимальное значение элементов массива: {np.max(arr)}', '\n')

# Создай массив от 10 до 50 с шагом 5.
arr = np.arange(10, 50, 5)

# Выведи элемент с индексом 2.
print(arr[2])

# Замени элемент с индексом 4 на 99 и выведи обновленный массив.
arr[4] = 99
print(arr, '\n')

# Создай массив из 20 случайных чисел от 0 до 100.
arr = np.random.randint(0, 101, size=20)

# Выведи только те элементы, которые больше 50.
print(arr[arr > 50])

# Замените все элементы, которые меньше 20, на 0 и выведи результат.
arr[arr < 20] = 0
print(arr, '\n')

# Создание графика с помощью библиотеки Matplotlib.
# Генерация случайных данных
np.random.seed(42)
x_data = np.arange(10)
y_data = np.random.randint(1, 101, size=10)

# Создание столбчатого графика
plt.figure(figsize=(8, 6))
plt.bar(x_data, y_data, color='skyblue', edgecolor='black')

# Подписи к осям и графику.
plt.title("Линейный график с помощью Matplotlib.")
plt.xlabel("Название оси X")
plt.ylabel("Название оси Y")

# Показать сетку
plt.grid(True, linestyle='--', alpha=0.5)

# Отображение графика.
plt.show()