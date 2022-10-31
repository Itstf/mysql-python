import mysql.connector
import time
import os
from produtos.exibir_produtos import exibir_produtos

def editar_produtos():
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
    
    exibir_produtos()
    
    print('\n')
    
    print('PRODUTOS CADASTRADOS DISPONIVEIS PARA ATUALIZAR')

    update_id = int(input('ID do produto a ser atualizado: '))
    print(update_id)

    time.sleep(1)
    os.system('cls')

    update_nome = input('Nome do produto atualizado: ')
    print(update_nome)
    
    time.sleep(1)
    os.system('cls')
    
    update_desc = input('Descrição atualizada: ')
    print(update_desc)

    time.sleep(1)
    os.system('cls')

    update = (
        "UPDATE produtos SET nome_produto = %s, desc_produto = %s WHERE idprodutos = %s"
    )
    dados = (f'{update_nome}', f'{update_desc}', f'{update_id}',)
    cursor.execute(update, dados)
    cnx.commit()
    
# editar_produtos()
  