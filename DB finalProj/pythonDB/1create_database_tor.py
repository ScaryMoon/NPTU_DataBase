import mysql.connector as mysql

account = mysql.connect(user="root", password="123456789", host="localhost")

cursor = account.cursor()
cursor.execute("CREATE DATABASE pyDB_01")
