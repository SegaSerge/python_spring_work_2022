import psycopg2

try:

    con = psycopg2.connect(
       database="students123",
       user="",
       password="",
       host="localhost",
       port="5432"
     )
    print("connect")
    curs = con.cursor()

    curs.execute("""CREATE TABLE "test" (
     "id_test" SERIAL PRIMARY KEY,
      "option" TEXT NOT NULL,
      "status" BOOLEAN
     )""")

    curs.execute("""CREATE TABLE "student" (
      "id_student" SERIAL PRIMARY KEY,
      "id_test" INTEGER NOT NULL,
      "name" VARCHAR(50) NOT NULL,
      "lastname" VARCHAR(50) NOT NULL,
      "patronymic" VARCHAR(50),
      "age" SMALLINT
    )""")

    curs.execute("""  CREATE INDEX "idx_student__id_test" ON "student" ("id_test") """)
    # curs.execute(""""ALTER TABLE "student" ADD CONSTRAINT "fk_student__id_test" FOREIGN KEY ("id_test")
    #   REFERENCES "test" ("id_test") """)

    con.commit()
except:
    print("no connect")
