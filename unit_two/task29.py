#todo Задача 2. Транспонирование матрицы, transpose(matrix)
#Написать функцию transpose(matrix), которая выполняет транспонирование матрицы.
# Решить с использованием списковых включений.

def transpose(mass):
    print([[row[i] for row in mass] for i in range(len(mass[0]))])




transpose([[1, 2, 3], [4, 5, 6]])

#[[1, 4], [2, 5], [3, 6]]
