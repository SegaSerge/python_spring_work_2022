import random
words = ["оператор", "конструкция", "объект"]
desc_ = ["Это слово обозначает наименьшую автономную часть языка программирования", "..", ".."]


def choise_words():
    return random.randint(0, 2)


k = choise_words()
print("ВНИМАНИЕ ВОПРОС!->>>",  desc_[k])
print("Крутите барабан!")

counter = 10
word = []
for x in range(0, len(words[k])):
    word.append("#")


def fun_counter():
    global counter
    counter -= 1
    return counter


def enter_alpha(alpha):
    global words
    global k

    lit = []
    start = 0

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
        fun_counter()


def test_alpha(alpha):
    #return True if (len(alpha) == 1 & (alpha in words[k])) else False
    #Если здесь сделать объединённую проверку, тогда из функции enter_alpha() можно убрать
    # проверку на наличие буквы в слове, но оставлю так, чтобы отдельно выводить ошибки
    return False if (len(alpha) != 1) else True


while counter > 0:
    if word != list(words[k]):
        alpha = input("Введите букву:")
        if test_alpha(alpha):
            enter_alpha(alpha)
            continue
        else:
            print("Вы ввели больше одной буквы или вообще не ввели букву!")
            #print(" Нет такой буквы в слове! У Вас осталось: ", counter, " попыток")
            #fun_counter()
    else:
        print("И это слово! -->", words[k], "<-- Поздравляю! Вы ВЫИГРАЛИ АВ-ТО-МО-БИЛЬ!")
        break

else:
    print("у Вас закончились попытки!")