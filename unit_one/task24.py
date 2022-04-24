import string

data = input("введите числа через пробел")

#alph = string.ascii_lowercase
alph = [" ", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n",
              "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
out_ = str()

for elem in data.split(" "):
    out_ += str(alph[int(elem)]) if elem.isalnum() else out_.join(elem)

print(out_)
