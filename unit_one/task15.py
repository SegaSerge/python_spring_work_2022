import random
k = random.randint(0, 2)
q = random.randint(0, 2)

words = ["оператор", "конструкция", "объект"]
desc_ = ["Это слово обозначает наименьшую автономную часть языка программирования", "..", ".."]
print("ВНИМАНИЕ ВОПРОС!->>>",  desc_[q])
print("Крутите барабан!")

counter = 10
lit = []
word = []
for x in range(0, len(words[k])):
    word.append("#")

while counter > 0:

    if word != list(words[k]):
        alpha = input("Введите букву:")
        start = 0
        if (len(alpha) > 1) | (len(alpha) == 0):
            print("Вы ввели больше одной буквы или вообще не ввели букву!")
            continue

        if alpha in words[k]:
            count = 0

            while count < words[k].count(alpha):
                start = words[k].index(alpha, start, len(words[k])) + 1
                lit.append(start - 1)
                count += 1
            else:
                for x in lit:
                    word[x] = alpha
                lit.clear()
                print(word)
        else:
            print(" Нет такой буквы в слове! У Вас осталось: ", counter, " попыток")
            counter -= 1
    else:
        print("И это слово! -->", words[k], "<-- Поздравляю! Вы ВЫИГРАЛИ АВ-ТО-МО-БИЛЬ!")
        break

else:
    print("у Вас закончились попытки!")