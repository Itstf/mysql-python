import mysql.connector

def cadastrar_produtos():
    # conectar bd
    cnx = mysql.connector.connect(
        user='root', 
        password='root',
        host='10.109.71.19',
        port=3306,
        database='thaiza_favarelli'
    )
    cursor = cnx.cursor()
    
    idproduto = str(input('id Produto: '))
    print(idproduto)
    
    nomeproduto = str(input('Nome do Produto: '))
    print(nomeproduto)
    
    descproduto = str(input('Descrição do Produto: '))
    print(descproduto)
    
    qtdproduto = int(input('Quantidade do Produto: '))
    print(qtdproduto)
    
    precoproduto = float(input('Preço do Produto: '))
    print(precoproduto)

    inserir = (
        "INSERT INTO produtos(idprodutos, nome_produto, desc_produto, qtd_produto, preco_produto)"
        "VALUES(%s, %s, %s, %s, %s)"
    )
    dados = (f'{idproduto}', f'{nomeproduto}', f'{descproduto}', f'{qtdproduto}', f'{precoproduto}')
    cursor.execute(inserir, dados)
    
    cnx.commit() # salvar 