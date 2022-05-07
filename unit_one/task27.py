import random
import pickle
# import keyboard
# попробывал сделать через keyboаrd - срабатывает только 1 раз и при этом игра не останавливается
# - решил оставить через ввод

main_flag = True
save_mass = {}
x = int()
number = int()
count = int()
save_r = []
# keyboard.add_hotkey(0x01, lambda: print("swewew"))
while main_flag:

    def start_game():
        global count, x, number, main_flag
        print("Wellcome to Game! Угадайте число от 0 до 100 за 10 попыток")
        print("istruction: Во время игры можно вызвать меню, введя 's'")
        print("Выберите один из вариантов :" + "\n" + "1. Новая Игра"
                  + "\n" + "2. Продолжить игру" + "\n" + "3. Выход ")
        st = int(input("Ваш выбор: "))

        match st:
            case 1:
                print("Игра началась! Удачи!")
                x = random.randint(0, 100)
                count = 10
                main_function()
                main_flag = True
            case 2:
                print("Продолжим игру")
                continue_game()
            case 3:
                main_flag = False

    def counter():
        global count
        count -= 1
        return count

    def save_game_file(count_, x_, num):
        global save_mass
        s_obj = {"count": count_, "number": x_, "last_number": num}
        save_mass[input("Введите имя для сохранения: ")] = s_obj
        with open("save_all.pkl", "ab") as f:
            pickle.dump(save_mass, f, pickle.HIGHEST_PROTOCOL)
        f.close()
        print("Игра сохранена!")

    def read_save_file():
        global save_mass, save_r
        save_r.clear()
        with open("save_all.pkl", "rb") as f:
            while True:
                try:
                    save_r.append(pickle.load(f))
                except EOFError:
                    break
        f.close()

    def start_continue(save):
        global count, x, number, save_mass, save_r
        for key in save:
            match key:
                case "count":
                    count = save[key]
                    #print(count, "<- count")
                case "number":
                    x = save[key]
                    #print(x, "<- x")
                case "last_number":
                    number = save[key]
                   # print(number, "<- numt")
        main_function()

    def continue_game():
        read_save_file()
        global save_r, main_flag
        print("----Выберите имя сохранения из списка---- ")
        print("Сохранения:")
        if len(save_r) == 0:
            print("Сохранений нет, продолжим игру? y/n (no-exit)")
            f = open("save_all.pkl", "wb")
            f.close()
            tur = input("Enter choise: ")
            match tur:
                case "y":
                    main_function()
                case "n":
                    main_flag = False
        else:
            for element in save_r:
                for key in element:
                    print(key)

            key = input("Ввод имени: ")
            for element in save_r:
                if key not in element:
                    continue
                else:
                    start_continue(element[key])
                    #print(element[key])

    def game(flag, count_):
        match flag:
            case 1:
                print("Введенное число меньше загаданного! у Вас ", count_, "попыток")
            case 2:
                print("Введенное число больше загаданного! у Вас ", count_, "попыток")
            case 3:
                print("Поздравляю! Вы угадали число за", 10 - count_, "попыток")
                print("\n")
                start_game()

    def num_(number_):
        if number_ < x:
            game(1, count)
        elif number_ > x:
            game(2, count)
        else:
            game(3, count)

    def str_enter(enter):
        global main_flag
        if enter == "s":
            print(" 1. Продолжить" + "\n" + " 2. Сохранить"
                           + "\n" + " 3. Запустить из сохранения " + "\n"
                           + " 4. Начать Сначала" + "\n" + " 5. Выход " + "\n")
            ch = int(input("Ваш выбор: "))
            match ch:
                case 1:
                    main_function()
                case 2:
                    save_game_file(count, x, number)
                    print(" 1. Продолжить" + "\n" + " 2. Выйти ")
                    tur = int(input("Ваш выбор: "))
                    match tur:
                        case 1:
                            main_function()
                        case 2:
                            main_flag = False
                case 3:
                    continue_game()
                case 4:
                    start_game()
                case 5:
                    main_flag = False

    def main_function():
        global count, x, number, main_flag
        while count > 0:
            enter_ = input("Введите число от 0 до 100: ")
            if enter_.isdigit():
                counter()
                number = int(enter_)
                num_(int(enter_))
            else:
                ent = str(enter_)
                str_enter(ent)
                break
            #print(x)
        else:
            print("Вы проиграли! У Вас закончились попытки!")
            print(" 1.Начать новую игру"+"\n"+" 2.Сохранения"+"\n"+" 3.Выход"+"\n")
            tur = int(input("Ваш выбор: "))
            match tur:
                case 1:
                    start_game()
                case 2:
                    continue_game()
                case 3:
                    main_flag = False

    start_game()

# keyboard.add_hotkey(0x01, lambda: str_enter("s"))
else:
    print("Спасибо за игру!")
