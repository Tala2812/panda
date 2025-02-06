import pandas as pd
import numpy as np


data = {
    'Имя': ['Ната', 'Костя', 'Оля', 'Макс', 'Катя', 'Андрей', 'Слава', 'Света', 'Кристина', 'Дима'],
    'Математика': [5, 4, 4, 3, 5, 5, 3, 4, 5, 4],
    'Физика': [4, 5, 5, 3, 3, 4, 4, 5, 4, 4],
    'Химия': [3, 5, 4, 5, 5, 5, 4, 5, 4, 3],
    'История': [4, 4, 4, 3, 5, 5, 5, 4, 4, 3],
    'Литература': [5, 5, 5, 5, 4, 4, 4, 5, 5, 3]
}

df = pd.DataFrame(data)
df.set_index('Имя', inplace=True)

print("Первые несколько строк DataFrame:")
print(df.head())


average_scores = df.mean(numeric_only=True)
print("\nСредняя оценка по каждому предмету:")
print(average_scores)


median_scores = df.median(numeric_only=True)
print("\nМедианная оценка по каждому предмету:")
print(median_scores)


Q1_math = df['Математика'].quantile(0.25)
Q3_math = df['Математика'].quantile(0.75)
IQR_math = Q3_math - Q1_math
print("\nQ1, Q3 и IQR для оценок по математике:")
print(f"Q1: {Q1_math}")
print(f"Q3: {Q3_math}")
print(f"IQR: {IQR_math}")


std_dev = df.std(numeric_only=True)
print("\nСтандартное отклонение по каждому предмету:")
print(std_dev)