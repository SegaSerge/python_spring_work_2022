# Задание необходимо ещё доделать(убрать лишнее и на общей БД запустить),
# переделал базы под себя. Скидываю код, чтобы видно было, что хоть что-то делаю...

import time
import datetime
import psycopg2

from threading import Thread, Lock


class Db:
    __instance__ = None

    def __init__(self):
        self.__con = psycopg2.connect(database="postgres", user="", password="", host="localhost", port=5432)
        # Проверяем конструктор на сущ. экземпляр
        if Db.__instance__ is None:
            Db.__instance__ = self.__con
        else:
            raise Exception("We can not creat another class")

    @staticmethod
    def get_instance():
        if not Db.__instance__:
            Db()
        return Db.__instance__

    # @staticmethod
    # def get_connect():
    #     return psycopg2.connect(database="postgres", user="", password="", host="localhost", port=5432)


class Profile:
    def __init__(self, name=None, lastname=None, age=None, password=None):
        self.conn = Db.__instance__
        self.name = name
        self.lastname = lastname
        self.age = age
        self.password = password
        self.login = None


    def get_profile(self, login):

        curs = self.conn.cursor()
        curs.execute(f"""SELECT "login" , "password" FROM "profile" where "login" LIKE '{login}' """)
        log_pass = curs.fetchall()
        return log_pass

    def set_profile(self, name, lastname, otch, group, login, password):
        curs = self.conn.cursor()
        curs.execute(f"""INSERT INTO "student" ("name", "lastname", "patronymic", "group") 
        VALUES ('{name}', '{lastname}', '{otch}', '{group}')""")
        self.conn.commit()

        curs.execute(f"""SELECT "id_student" FROM "student" 
        where "name" LIKE '{name}' and "lastname" LIKE '{lastname}' """)
        id_student = curs.fetchall()

        curs.execute(f"""INSERT INTO "profile" VALUES ('{login}','{password}','{id_student[0][0]}') """)
        self.conn.commit()
        #self.conn.close()


class Auth:
    LOGIN = None
    def __init__(self):
        self.conn = Db.__instance__
        self.login = None
        self.password = None
        self.name = None
        self.lastname = None
        self.patronymic = None
        self.group = None
        self.age = None
        self.tel = None
        self.email = None
    """Класс содержит методы регистрации, захода в систему и выхода из нее"""
    is_auth = bool()

    def registration(self):
        self.login = input("login: ")
        self.password = input("password: ")
        self.name = input("name: ")
        self.lastname = input("lastname: ")
        self.patronymic = input("patronymic: ")
        self.group = input("group: ")
        self.age = input("age: ")
        self.tel = input("tel: ")
        self.email = input("email: ")

        Profile().set_profile(self.name, self.lastname, self.patronymic, self.group, self.login, self.password)
        Auth.LOGIN = self.login
        self.conn.close()
        Auth.is_auth = True
        return Auth.is_auth

    def log_in(self):
        print("Enter your:")
        self.login = input("login: ")
        self.password = input("password: ")
        prof = Profile().get_profile(self.login)
        Auth.LOGIN = self.login
        if len(prof):
            if self.password == str(prof[0][1]):
                Auth.is_auth = True
                return Auth.is_auth
            else:
                print("wrong password"), Auth().log_in()
        else:
            print("Профиль не найден! пройдите регистрацию!")
            Auth().registration()

    def logout(self):
        Auth.is_auth = False


class SaveResult:

    def __init__(self):
        self.conn = Db.get_instance()
        self.login = Auth.LOGIN
        self.curs = self.conn.cursor()

    def save_result(self, test, d_time, result, timer):
        self.curs.execute(f"""INSERT INTO "test_result" ("login", "dt_time", "test", "result", "tm_test") 
                VALUES ('{self.login}','{d_time}', '{test}', '{result}', '{timer}')""")
        self.conn.commit()


class Test:
    def __init__(self):
        self.conn = Db.get_instance()

    """ В классе реализуем методы работы с БД """

    def get_list_tests(self):
        curs = self.conn.cursor()
        curs.execute(""" SELECT "id_test", "theme" FROM "test" """)
        tests = curs.fetchall()
        return tests

    def get_questions(self, id_test):
        curs = self.conn.cursor()
        curs.execute(f""" SELECT "id_question", "id_answer", "status" FROM "test_question" 
                                WHERE "id_test" = {id_test} """)
        test = curs.fetchall()
        return test


class TestSystem:
    def __init__(self):
        self.conn = Db.get_instance()
        self.curs = self.conn.cursor()
    t_out = False

    "Класс взаимодействует с моделью и представлением. Включает всю бизнес логику системы."
    def run(self):

        while not Auth.is_auth:
            Auth().log_in()
        else:
            print("Вы Вошли в систему Тестирования!", "\n",
                  "Для Начала теста выберете Тему и тест начнётся!", "\n",
                  "У Вас 5 минут на решение теста")
            TestView().render()
        """Метод реализует запуск теста"""

    def show_list(self):
        """Метод реализует вывод списка тестов на экран"""
        pass

    def show_question(self, id_question):
        pass
        """Метод реализует вывод списка тестов на экран"""

    def get_list_questions(self, elem):

        self.curs.execute(f""" SELECT "text_question" FROM "question" WHERE "id_question" = {elem} """)
        test = self.curs.fetchall()
        return test

    def get_list_answer(self, elem):
        self.curs.execute(f""" SELECT "answer" FROM "answer" WHERE "id_answer" = {elem} """)
        answers = self.curs.fetchall()
        return answers


class View:
    """ 'Абстрактный' класс для потомков """
    def render(self):
        pass


class QuestionView(View):
    """В классе перегружаем виртуальный метод  render от родителя"""

    lock = Lock()
    stop_thread = False

    def render(self, data=None):
        stud_result = 0
        q = list()
        q1 = list()
        q2 = list()
        list_question = Test().get_questions(data)

        for qust1, qust2, qust3 in list_question:
            q.append(qust1)  # вопрос
            q1.append(qust2)  # ответ
            q2.append(qust3)  # тру/фолс

        quest = sorted(set(q))

        k_a = len(q1) / len(quest)
        k = 0
        # вывод вопроса по id
        for elem in quest:
            c = 1
            test1 = TestSystem().get_list_questions(elem)
            for t in test1:
                print("Вопрос: ", str(t).strip("( ) , ' "))

            # вывод и чтение ответов
            for i in range(k, int(k + k_a)):
                ans1 = TestSystem().get_list_answer(q1[i])
                print(f"{c}. ", str(ans1[0]).strip("(),'"))
                c += 1

            stud_answer = int(input("Enter yuor answer: "))
            stud_result += 1 if q2[stud_answer - 1 + k] is True else None
            k += int(k_a)
        return stud_result

    def t_render(self, data):
        st_r = list()

        d_time = datetime.datetime.now()
        t_f_time = time.time()
        th = Thread(target=(st_r .append(QuestionView().render(data))))
        th.start()
        QuestionView.lock.acquire()
        QuestionView.stop_thread = True
        QuestionView.lock.release()

        test_time = time.time() - t_f_time
        SaveResult().save_result(data, d_time, st_r, test_time)
        print("Поздравляю! Ваш тест завершён!", "\n" "Ваша оценка: ", st_r)
        time.sleep(5)
        Auth().logout()

    """Метод реализует отрисовку вопроса с вариантами ответа и строкой выбора варианта"""


class TestView(View):
    def __init__(self):
        pass

    def render(self):
        for test in Test().get_list_tests():
            print(str(test).strip("( ) , ' ").replace(", '", ". "))
        QuestionView().t_render(input("Enter number of test: "))

    # """Метод реализует отрисовку экранной формы выбора билета """


TestSystem().run()


class RegistrationView(View):
    """В классе перегружаем виртуальный метод  render от родителя"""

    def render(self, data):
        """Метод реализует отрисовку регистрации пользователя"""


class LoginView(View):
    """В классе перегружаем виртуальный метод  render от родителя"""

    def render(self, data):
        """Метод реализует отрисовку входа по логину и паролю для зарегистрированного пользователя"""
