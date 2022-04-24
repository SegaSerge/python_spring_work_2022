
f = open("message.txt", "r")
all = f.readlines()
f.close()

alphavit = ["а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л",
            "м", "н", "о", "п", "р", "с", "т", "у", "ф", "х", "ц",
            "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я"]


def get_nub(a, num):
    
    lit = alphavit[-32 + alphavit.index(a) + num]
    #print(a, "---- буква ввода")
    #print(id, " --- ID буквы в алфавите")
    #print(lit, "---- замена буквы")
    return lit


def red_line(line):
    line1_ = str()
    for line_ in line.upper().strip("9 4 2 XXIII\n").split(" "):
        line1_ += line_.strip(". ,( ) -") + " "
    return line1_.lower()


def passw(line_):
    out1 = str()
    for word in red_line(line_).split(" "):
        for al in word:
            out1 += (get_nub(al, all.index(line_)))
        out1 += " "
    return out1


for line in all:
    print("OUT:")
    print(passw(line))
    print("Start:")
    print(line)
