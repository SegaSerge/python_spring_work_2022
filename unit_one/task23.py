import string
f = open("message1.txt", "r")
password = f.readlines()
f.close()

alphavit = string.ascii_lowercase
#alphavit = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n",
            #  "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]


def get_nub(a, num):
    k = len(alphavit)
    lit = alphavit[-k + alphavit.index(a) + num]
    # print(a, "---- буква ввода")
    # print(id, " --- ID буквы в алфавите")
    # print(lit, "---- замена буквы")
    return lit


def read_line(line):
    words = str()
    for word in line.split(" "):
        words += word.strip(".") + "1"
    return words

def ps_words(password):
    out_ = str()
    for line in password:
        for i in range(0, len(alphavit)):
            for elem in read_line(line):
                if elem == "'":
                    continue
                elif elem == "1":
                    out_ += " "
                    continue
                out_ += get_nub(elem, i)
            print(out_)
            print("сдвиг: ", i)
            out_ = str()


ps_words(password)
