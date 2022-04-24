data = input("введите текст для создания алфавита!")

sdata = str()

for element in data:
    if element.isalpha() & (sdata.find(element) == -1):
        sdata += element
    else:
        continue
print(sdata.lower())
