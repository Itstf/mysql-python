import mysql.connector
import time
import os
from produtos.exibir_produtos import exibir_produtos

def excluir_produto():
    # conectar bd
    cnx = mysql.connector.connect(
        user='root', 
        password='root',
        host='10.109.71.19',
        port=3306,
        database='thaiza_favarelli'
    )
    cursor = cnx.cursor()

    time.sleep(1)
    os.system('cls')
    
    print('Produtos cadastrados: \n')
    exibir_produtos()
    
    del_id = int(input('\nEscolha o ID do produto a ser excluido: '))
    
    delete = "DELETE FROM produtos WHERE idprodutos = %s"
    dados = (f'{del_id}',)
    cursor.execute(delete, dados)
    cnx.commit()

# excluir_produto()