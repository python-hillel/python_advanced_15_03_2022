import sqlite3

from faker import Faker

from variables import DB_NAME

connection = sqlite3.connect(DB_NAME)

with open('schema.sql') as file:
    connection.executescript(file.read())

cursor = connection.cursor()

f = Faker()
for _ in range(25):
    title = f.word()
    author = f'{f.last_name()} {f.first_name()}'
    cursor.execute("INSERT INTO books (title, author) VALUES (?, ?)", (title, author))

connection.commit()
connection.close()
