import sqlite3
connection = sqlite3.connect('todo.sqlite3')

cursor = connection.cursor()

sql = '''
create table vendaDetalhe (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    vendaId INTEGER,
    quantidade INTEGER,
    valor INTEGER,
    produtoId
        FOREIGN KEY (vendaId) REFERENCES venda(vendaId)
        FOREIGN KEY (produtoId) REFERENCES produto(id)
)
'''

cursor.execute(sql)
connection.commit()
connection.close()
