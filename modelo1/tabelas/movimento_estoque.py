import sqlite3
connection = sqlite3.connect('todo.sqlite3')

cursor = connection.cursor()

sql = '''
create table movimentoEstoque (
    id INTENGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    estoqueProdutoId INTENGER,
    quantidade INTENGER,
    data DATETIME,
    tipoMovimentoId INTENGER,
    vendaDetalheId INTENGER,
        FOREIGN KEY (tipoMovimentoId) REFERENCES tipoMovimento(id)
        FOREIGN KEY (vendaDetalheId) REFERENCES vendaDetalhe(id)
)
'''

cursor.execute(sql)
connection.commit()
connection.close()
