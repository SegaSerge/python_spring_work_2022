lines = list()
summ = 133


f = open("import_this.txt", "r")
f.seek(0, 0)
for line in f:
    lines.append(line)
    if not line:
        break
f.close()
print(lines[::-1])

'''
summ = 0

for i in range(0, len(lines)):
    summ += len(lines[i])
print(summ)
'''

f1 = open("import_this.txt", "at+")
f1.seek(summ)
f1.write("\n" + "Вывод123:" + "\n")
f1.writelines(lines[::-1])
f1.close()
