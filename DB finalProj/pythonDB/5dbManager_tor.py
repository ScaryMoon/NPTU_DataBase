import mysql.connector as mysql


class Manager:
    def __init__(self, user, password, host, database):
        self.account = mysql.connect(
            user=user, password=password, host=host, database=database)
        self.cursor = self.account.cursor()

    def insert_student(self, student_info):
        sql = "INSERT INTO Students (StudentID,Name,City) VALUE(%s,%s,%s)"
        self.cursor.execute(sql, student_info)  # every one's id name city

    def showUp(self, table_name):
        self.cursor.execute(f"SELECT * FROM {table_name}")
        everyone = self.cursor.fetchall()
        for student in everyone:
            print(student)


dbManager = Manager("root", "123456789", "localhost", "pydb_01")
# insert
students = [
    (6, "minecraft", "canada"),
    (7, "APEX", "NoChina")
]
# for student in students:
#     dbManager.insert_student(student)
dbManager.showUp("students")
dbManager.account.commit()  #資料庫重新整理
