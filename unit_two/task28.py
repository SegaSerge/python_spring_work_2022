import time
import datetime

A = [31, 4, 59, 26, 41, 58, 1, -20, 100]
print("Starting mass: ", A)
count = int()
last = datetime.time()
name = str()
name_1 = str()


def decor_save(*info):
    global count
    with open("debug.log", "at") as f:
        for elem in info:
            f.write(str(elem) + ", ")
        else:
            f.write("\n")
            f.close()
            count = 0


def decorator_counter(func):
    global count, last, name_1

    def wrapper(*args, **kwargs):
        global count, last, name_1

        func(*args, **kwargs)
        count += 1
        last = datetime.datetime.today().strftime("%d.%m.%Y ---- %H:%M:%S")
        name_1 = func.__name__

    return wrapper


def decorator_render(func):
    global name

    @decorator_counter
    def wrapper(text):
        global name

        start = time.time()
        func(text)
        end = time.time()
        #print("Time :", (end - start), "seconds", " count= ", count)
        name = func.__name__

    return wrapper


@decorator_render
def insertion_sort(mass):
    for j in range(1, len(mass)):
            key = mass[j]
            i = j - 1
            while (i >= 0) & (mass[i] < key):
                    mass[i+1] = mass[i]
                    i -= 1
            mass[i+1] = key
    return mass


@decorator_render
def merge_sort(numbers):
    if len(numbers) > 1:
        delen = len(numbers)//2
        a = numbers[:delen] # первая половина массива
        b = numbers[delen:] #вторая половина массива
        merge_sort(a)
        merge_sort(b)
        i = j = k = 0 # индексы в списках a, b, numbers
        while i < len(a) and j < len(b):
            if a[i] < b[j]:
                numbers[k] = a[i]
                i += 1
            else:
                numbers[k] = b[j]
                j += 1
            k += 1

        while i < len(a):
            numbers[k] = a[i]
            i += 1
            k += 1
        while j < len(b):
            numbers[k] = b[j]
            j += 1
            k += 1


@decorator_counter
def test():
    k = 0
    while k < 2:
        time.sleep(0.1)
        k += 1
    return k


insertion_sort(A)
decor_save(name, count, last)

merge_sort(A)
decor_save(name, count, last)

test()
decor_save(name_1, count, last)
