ke = list()
page = {"title": "Тег BODY",
        "charset": "utf-8",
        "alert": "Документ загружен",
        "p": "Ut wisis enim ad minim veniam,  suscipit lobortis nisl ut aliquip ex ea commodo consequat."}

lines = list()

f = open("index.html", "r+")
for line in f:
    lines.append(line)
    if not line:
        break
f.close()


print(lines)
lines_new = list()
for line in lines:
    for key in page:
        if key in line:
            print(lines.index(line))
            id = line.find("?")
            print(line[:id] + page[key] + line[id + 1:])
            lines_new.append(str(line[:id]) + str(page[key]) + str(line[id + 1:]))
            break
    else:
        lines_new.append(lines[lines.index(line)])


f = open("index.html", "at+")
f.writelines(lines_new)
f.close()
