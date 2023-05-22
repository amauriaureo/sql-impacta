import sqlite3
connection = sqlite3.connect('todo.sqlite3')

cursor = connection.cursor()

sql = '''
create table vendaDetalhe (
    id INTENGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    vendaId INTENGER,
    quantidade INTENGER,
    valor INTENGER,
    produto.Id
        FOREIGN KEY (vendaId) REFERENCES venda(vendaId)
        FOREIGN KEY (produtoId) REFERENCES produto(id)
)
'''

cursor.execute(sql)
connection.commit()
connection.close()
