# Не сделал метод put, параллельно подключил ТестСистему, чтобы был доступ к базе
#Если делать всё через json - всё работает, но из-за изменения ссылки - пишет Metod NOT ALLOWED

from flask import Flask, request, jsonify
from flask_restx import Api, Resource, reqparse
import threading


app = Flask(__name__)
api = Api(app)


@api.route('/hello')
class HelloWorld(Resource):

    def get(self):
        return 'hello'

    def post(self):
        return "POST"


@api.route('/student/<id>')
class Student(Resource):
    def __init(self):
        pass

    def get(self, id):
        """ Получаем студента по его id """
        content = request.json
        # Return data as JSON
        from task35 import Db
        curs = Db.get_connect().cursor()
        curs.execute(f"""SELECT "login","name", "lastname", "email", "tel"
                             FROM profile WHERE "id_profile"={content['id']}""")
        stud_list = curs.fetchall()
        for login, name, lastname, email, tel in stud_list:
            return list(("login:", f"{login}", "name:", f"{name}", "lastname:", f"{lastname}"))

    #router /student/{id}
    def post(self, id):
        """ Передаем изменения в json """
        change = request.json
        from task35 import Db
        conn = Db.get_connect()
        curs = conn.cursor()
        curs.execute(f"""UPDATE public.profile SET "login"='{change['login']}', "name" = '{change['name']}', 
        "lastname" = '{change['lastname']}'
        WHERE id_profile = {id}""")
        conn.commit()
        return "GOOD Change"

    # router /student/
    @app.route('/student/')
    def put(self):
        """ Добавить студента в json """
        change = request.json
        from task35 import Db
        conn = Db.get_connect()
        curs = conn.cursor()
        password_hashed = 1234
        curs.execute(f"""INSERT INTO "profile" ("name", "lastname", "id_group", "login", "password", "email") 
                    VALUES ('{change['name']}', '{change['lastname']}', '1', '{change['login']}', '{password_hashed}', 
                    '{change['email']}')""")
        conn.commit()
        return "GOOD into"

    # router /student/{id}
    def delete(self, id):
        """ Удалим студента по {id}"""
        from task35 import Db
        conn = Db.get_connect()
        curs = conn.cursor()

        curs.execute(f"""DELETE FROM profile WHERE id_profile={id}""")
        conn.commit()
        return f"GDELETE id = {id}"


def worker():
    from task35 import TestSystem
    TestSystem().run()


def worker1():
    app.run()


if __name__ == '__main__':
    th2 = threading.Thread(target=worker)
    th1 = threading.Thread(target=worker1)
    if True:
        th2.start()
        th1.start()





    #th1 = threading.Thread(target=HelloWorld(Resource).get)
    # th3 = threading.Thread(target=app.run())
    # th3.start()

    #th2 = threading.Thread(target=worker)
    #
    #t
    #th3.start()
    #th1.start()
    #app.run()

