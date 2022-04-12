#Единицы массы пронумерованы следующим образом: 1 — килограмм, 2 — миллиграмм, 3 — грамм, 4 — тонна, 5 — центнер.
#Дан номер единицы массы и масса тела M в этих единицах (вещественное число). Вывести массу данного тела в килограммах.
# Данную задачу нужно решить с помощью конструкции  match  (Python v3.10)

# Пример:
# Введите единицу массы тела
#       1 - килограмм
#       2 — миллиграмм
#       3 — грамм
#       4 — тонна
#       5 — центнер

print("Enter a unit of body mass: "
      " 1-kilogram"
      " 2-milligram"
      " 3-gram"
      " 4-ton"
      " 5-centner")
unit_ = int(input("enter a unit of body mass:"))
mass = int(input("Enter of body mass:"))
match unit_:
    case 1:
        print("Body mass = ", mass, "kg")
    case 2:
        print("Body mass = ", mass * (10 ** (-6)), "kg")
    case 3:
        print("Body mass = ", mass * (10 ** (-3)), "kg")
    case 4:
        print("Body mass = ", mass * 1000, "kg")
    case 5:
        print("Body mass = ", mass * 100, "kg")
