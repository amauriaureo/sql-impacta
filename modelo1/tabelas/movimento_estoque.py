import sqlite3
connection = sqlite3.connect('todo.sqlite3')

cursor = connection.cursor()

sql = '''
create table movimentoEstoque (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    estoqueProdutoId INTENGER,
    quantidade INTEGER,
    data DATETIME,
    tipoMovimentoId INTEGER,
    vendaDetalheId INTEGER,
        FOREIGN KEY (tipoMovimentoId) REFERENCES tipoMovimento(id)
        FOREIGN KEY (vendaDetalheId) REFERENCES vendaDetalhe(id)
)
'''

cursor.execute(sql)
connection.commit()
connection.close()
