import sqlite3
connection = sqlite3.connect('todo.sqlite3')

cursor = connection.cursor()

sql = '''
create table EstoqueProduto (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    produtoId VARCHAR(20),
        FOREIGN KEY (produtoId) REFERENCES produto(id)
)
'''

cursor.execute(sql)
connection.commit()
connection.close()
