# todo: Проверить истинность высказывания: "Данное четырехзначное число читается одинаково
# слева направо и справа налево".
numb = input("Enter number")

if numb == numb[::-1]:
    print("True")
else:
    print("False")