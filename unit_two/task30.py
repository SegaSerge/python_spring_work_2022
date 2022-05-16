#Чтение из файла работает при условии, если там прописана матрица в формате как вв задании!
#P.S [[1, 2, 3], [4, 5, 6]]

matrix = [[1, 2, 3], [4, 5, 6]]


def load_matrix(f_name):
    with open(f_name, "r") as f:
        line = f.readline().strip("\n"+" []").split(",")
        f.close()
    return [l.strip(" []").split(",") for l in line]


def msum(ms):
    sum = 0
    for i in [col for row in ms for col in row]:
        sum += int(i)
    return print("суммa всех элементов матрицы: ", sum)

msum(matrix)
#21
msum(load_matrix('matrix.txt'))
#423
