import sqlite3
connection = sqlite3.connect('todo.sqlite3')

cursor = connection.cursor()

sql = '''
create table venda (
    vendaId INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    data DATETIME,
    valorTotal INTEGER,
    desconto INTEGER,
)
'''

cursor.execute(sql)
connection.commit()
connection.close()
