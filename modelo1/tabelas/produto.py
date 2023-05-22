import sqlite3
connection = sqlite3.connect('todo.sqlite3')

cursor = connection.cursor()

sql = '''
create table Produto (
    id INTENGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    nome VARCHAR(20)
)
'''

cursor.execute(sql)
connection.commit()
connection.close()
