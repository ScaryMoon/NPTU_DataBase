import mysql.connector as mysql

account = mysql.connect(user="root", password="123456789",
                        host="localhost", database="pyDB_01")

cursor = account.cursor()
cursor.execute("SELECT * FROM Students")

students = cursor.fetchall()
for student in students:
    print(student)


account.commit()  # DB更新
account.close()  # DB關閉
