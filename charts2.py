import numpy as np
import matplotlib.pyplot as plt

# Генерация двух наборов случайных данных
num_samples = 100
x_data = np.random.rand(num_samples)
y_data = np.random.rand(num_samples)


plt.scatter(x_data, y_data, c='blue', alpha=0.5, edgecolors='w', s=50)


plt.title('Диаграмма рассеяния случайных данных')
plt.xlabel('X данные')
plt.ylabel('Y данные')


plt.show()