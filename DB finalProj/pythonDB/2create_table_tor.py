import mysql.connector as mysql
account = mysql.connect(
    user="root", password="123456789", host="localhost", database="pyDB_01")

cursor = account.cursor()
cursor.execute(
    "CREATE TABLE Students (StudentID int PRIMARY KEY,Name VARCHAR(255),City VARCHAR(255))")
