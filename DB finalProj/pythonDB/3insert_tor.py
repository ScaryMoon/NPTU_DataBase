import mysql.connector as mysql

account = mysql.connect(user="root", password="123456789",
                        host="localhost", database="pyDB_01")

cursor = account.cursor()

sql = "INSERT INTO Students (StudentID,Name,City) VALUE(%s,%s,%s)"
students = [
    (1, "Annna", "Taiwan"),
    (2, "gura", "USA"),
    (3, "Inna", "engliand"),
    (4, "bae", "franch"),
    (5, "camame", "japan")
]
for student in students:
    cursor.execute(sql, student)


# 更新
account.commit()
