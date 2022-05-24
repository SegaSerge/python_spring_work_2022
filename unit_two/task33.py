import psycopg2
import bcrypt

try:
    conn = psycopg2.connect(
        database="students123",
        user="",
        password="",
        host="localhost",
        port="5432"
    )
    curs = conn.cursor()
    print("connect")
except:
    print("NO CONNECT!")


def start():
    print(" 1. Вход \n 2. Регистрация")
    ch = int(input("Выбор: "))
    match ch:
        case 1:
            enter()
        case 2:
            regist()


def regist():
    global curs
    print("Такого пользователя нет! пройдите регистрацию")
    login = str(input("login: "))
    password_hashed = str(bcrypt.hashpw(bytes(str(input("password: ")), encoding="utf8"),
                                        bcrypt.gensalt())).strip("' b")
    print(password_hashed)
    email = str(input("email: "))
    tel = str(input("tel: "))
    name = str(input("name: "))
    lastname = str(input("lastname: "))
    group = str(input("group: "))

    curs.execute(f""" INSERT INTO "user_log" ("login", "password", "mail", "tel", "name", "last_name", "group")
                    VALUES('{login}', '{password_hashed}', '{email}', '{tel}', '{name}', '{lastname}', '{group}');""")
    conn.commit()


def enter():
    print("Введите: ")
    login = str(input("login: "))
    ps = str(input("password: "))

    curs.execute(f"""SELECT "password", "name", "last_name" FROM "user_log" where "login" LIKE '{login}' """)
    qwe = curs.fetchall()
    if len(qwe) == 0:
        regist()
    else:
        for password, name, lastname in qwe:
            tf = (bcrypt.checkpw(ps.encode(), bytes(password, encoding="utf8")))
            print("Добро пожаловать!", name, " ", lastname) if tf else print("Wrong password"), enter()


start()


