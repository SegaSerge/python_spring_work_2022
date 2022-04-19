prices = {"banana": 4, "apple": 2, "orange": 1.5, "pear": 3}


def compute_bill(prices_):
  chek = dict()
  summ = 0
  for key in prices_:
    print(key)
    chek[key] = float(input("количество")) * prices_[key]
    summ += chek[key]

  return summ

print("Итоговая сумма в чеке: ", compute_bill(prices))
