# INSERTION_SORT - var 1 (по убыванию)

A = [31, 4, 59, 26, 41, 58, 1, -20, 100, -7]

print("Starting mass: ", A)


def insertion_sort(mass):
    for j in range(1, len(mass)):
            key = mass[j]
            i = j - 1
            while (i >= 0) & (mass[i] < key):
                    mass[i+1] = mass[i]
                    i -= 1
            mass[i+1] = key
    return mass


print("insertion_sort: ", insertion_sort(A))
