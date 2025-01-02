import sqlite3
import random
connection=sqlite3.connect('not_telegram.db')
cursor=connection.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)    
''')
cursor.execute("SELECT COUNT(*) FROM Users")
total1=cursor.fetchone()[0]
print('всего пользователей:', total1)
cursor.execute("SELECT SUM(balance) FROM Users")
total2=cursor.fetchone()[0]
cursor.execute("SELECT AVG(balance) FROM Users")
total3=cursor.fetchone()[0]
print('Средний баланс:', total3)
connection.commit()
connection.close()