# import mysql.connector
# import os
# import time

# def new_pedido():
#     # inserir um registro na tablea pedidos
#     # fazer um select com last_new_id
#     # armazenar esse id numa variavel
#     # listar os produtos cadastrados
#     # perguntar pro user qual ele deseja adicionar pelo id
#     # perguntar a qtd
#     # e inserir na tablea pedido_item
    
#     cnx = mysql.connector.connect(
#         user='root', 
#         password='root',
#         host='10.109.71.19',
#         port=3306,
#         database='thaiza_favarelli'
#     )
#     cursor = cnx.cursor()
    
#     # pedido-itens
#     id_produto = int(input('Insira o ID do produto: '))
#     qtd = int(input('Quantidade do produto: '))

#     criar_pedido = (
#         "INSERT INTO produtos(idprodutos, qtd)"
#         "VALUES(%s, %s)"
#     )
#     dados = ()
#     cursor.execute(criar_pedido, dados)
#     cnx.commit()
    
#     # pedidos
#     id = int(input('Insira o ID do pedido: '))
#     nome_cliente = int(input('Nome do cliente: '))

#     criar_pedido = (
#         "INSERT INTO produtos(idpedidos, nome_cliente)"
#         "VALUES(%s, %s)"
#     )
#     dados = ()
#     cursor.execute(criar_pedido, dados)
#     cnx.commit()