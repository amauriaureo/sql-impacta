import sqlite3
connection = sqlite3.connect('todo.sqlite3')

cursor = connection.cursor()

sql = '''
create table venda (
    vendaId INTENGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    data DATETIME,
    valorTotal INTENGER,
    desconto INTENGER,
)
'''

cursor.execute(sql)
connection.commit()
connection.close()
