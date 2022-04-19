game = list()
#game1 = dict()

for key in range(2, 13):
    on_off = True
    game.clear()
    while on_off:
        for x in range(1, 7):
            for y in range(1, 7):
                if key == (x + y):
                    game.append((x, y))
        else:
            print("Сумма: ", key, " Комбинация: ", game)
            #game1[key] = game
            on_off = False


#print(game1)
