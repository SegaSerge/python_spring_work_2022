mass = [1, 2, 17, 54, 30, 89, 2, 1, 6, 2]

x = int(input("enter number:"))
y = []
z = []
if x in mass:
    counter = 0
    start = 0
    if mass.count(x) == 1:
        print("В данном массиве только одно значение! и его индекс: ", mass.index(x))

    else:
        while counter < mass.count(x):
            start = mass.index(x, start, len(mass)) + 1
            counter += 1
            y.append(start - 1)
else:
    print("NO number in massive")

for i in range(0, len(y)-1):
    z.append(y[i+1] - y[i])

for i in range(0, len(y)-1):
    if y[i+1] - y[i] == min(z):
        print("индексы двух ближайших чисел из этого массива: ", y[i], " и ", y[i+1])